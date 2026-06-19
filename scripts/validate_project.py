#!/usr/bin/env python3
"""Validate NativeCAM project tree (lathe focus). Run from repo root or anywhere."""
import ast
import configparser
import os
import re
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG_LATHE = os.path.join(ROOT, 'cfg', 'lathe')
LIB_LATHE = os.path.join(ROOT, 'lib', 'lathe')
LIB_UTIL = os.path.join(ROOT, 'lib', 'utilities')
MENU = os.path.join(ROOT, 'catalogs', 'lathe', 'menu.xml')

sys.path.insert(0, ROOT)

errors = []
warnings = []
passed = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def ok(msg):
    passed.append(msg)


def parse_cfg(path):
    c = configparser.ConfigParser()
    f = open(path).read()
    f = re.sub(r'_\("', '', f)
    f = re.sub(r'"\)', '', f)
    f = re.sub(r'(?m)^(\ |\t)', r'\1.', f)
    c.read_string(f)
    return {s: {i: re.sub(r'(?m)^\.', '', ' ' + c.get(s, i, raw=True))[1:]
              for i in c.options(s)} for s in c.sections()}


def main():
    print('NativeCAM validate_project')
    print('ROOT =', ROOT)
    if not os.path.isfile(os.path.join(ROOT, 'ncam.py')):
        err('ncam.py not found — run inside nativecam-py3-gtk3 clone')
        print('\nClone first:')
        print('  git clone -b devel https://github.com/cnc-proton/nativecam-py3-gtk3.git')
        print('  cd nativecam-py3-gtk3')
        print('  python3 scripts/validate_project.py')
        return 1

    # lathe_polyline
    try:
        import lathe_polyline
        boot = lathe_polyline.bootstrap_defaults()
        for need in ('#<in_polyline>', '#<_mill_data_start>'):
            if need not in boot:
                err('bootstrap missing ' + need)
        ok('lathe_polyline.py')
        for rel in lathe_polyline.CFG_MANIFEST:
            if not os.path.isfile(os.path.join(ROOT, 'cfg', rel)):
                err('missing cfg: ' + rel)
        for name in lathe_polyline.NGC_MANIFEST:
            if not os.path.isfile(os.path.join(LIB_LATHE, name)):
                err('missing ngc: ' + name)
        if not [e for e in errors if e.startswith('missing')]:
            ok('lathe manifest files on disk')
    except Exception as e:
        err('lathe_polyline: ' + str(e))

    # cfg parse
    if os.path.isdir(CFG_LATHE):
        for fn in sorted(os.listdir(CFG_LATHE)):
            if fn.endswith('.cfg'):
                try:
                    parse_cfg(os.path.join(CFG_LATHE, fn))
                    ok('cfg ' + fn)
                except Exception as e:
                    err(fn + ': ' + str(e))

    # menu
    if os.path.isfile(MENU):
        try:
            from lxml import etree
            m = open(MENU).read()
            m = re.sub(r'_\(', '', m)
            m = re.sub(r'\)_', '', m)
            etree.fromstring(m)
            ok('menu.xml')
        except ImportError:
            warn('pip install lxml for menu.xml check')
        except Exception as e:
            err('menu.xml: ' + str(e))

    # ngc sub balance + calls
    lib_subs = set()
    for d in (LIB_LATHE, LIB_UTIL):
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith('.ngc'):
                continue
            t = open(os.path.join(d, fn)).read()
            for m in re.finditer(r'o<([a-zA-Z0-9_]+)>\s+sub\b', t, re.I):
                lib_subs.add(m.group(1).lower())
            opens = len(re.findall(r'o<[^>]+>\s+sub\b', t, re.I))
            closes = len(re.findall(r'o<[^>]+>\s+endsub\b', t, re.I))
            if opens != closes and d == LIB_LATHE:
                err('%s: sub/endsub mismatch' % fn)

    call_re = re.compile(r'o<([a-z_0-9]+)>\s+(?:CALL|call)\b', re.I)
    skip = {'select', 'get_max', 'get_offsets', 'line', 'rotate_xy',
            'set_feed_rate_and_speed', 'probe', 'poly_add_item',
            'lathe_path_walk', 'lathe_poly_create', 'lathe_xz_move',
            'lathe_rough_step', 'lathe_rough_step_id',
            'lathe_rough_pattern', 'lathe_rough_pattern_id'}
    if os.path.isdir(CFG_LATHE):
        for fn in os.listdir(CFG_LATHE):
            if not fn.endswith('.cfg'):
                continue
            conf = parse_cfg(os.path.join(CFG_LATHE, fn))
            g = ''
            for k in ('DEFINITIONS', 'BEFORE', 'CALL', 'AFTER'):
                if k in conf:
                    g += conf[k].get('content', '')
            for m in call_re.finditer(g):
                n = m.group(1).lower()
                if n.startswith('#') or n in skip:
                    continue
                if n not in lib_subs:
                    err('%s: unknown o<%s>' % (fn, n))
    ok('NGC cross-ref scan done')

    try:
        ast.parse(open(os.path.join(ROOT, 'ncam.py')).read())
        ok('ncam.py syntax')
    except SyntaxError as e:
        err('ncam.py: ' + str(e))

    print('\n' + '=' * 50)
    print('PASSED:', len(passed))
    print('WARNINGS:', len(warnings))
    print('ERRORS:', len(errors))
    for w in warnings:
        print(' !', w)
    for e in errors:
        print(' X', e)
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
