#!/usr/bin/env python3
"""Post-agent validation runner for NativeCAM."""

from __future__ import print_function

import argparse
import os
import re
import subprocess
import sys
import tempfile
from configparser import RawConfigParser
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
PYTHON_FILES = [
    ROOT / "ncam.py",
    ROOT / "lathe_polyline.py",
    ROOT / "pref_edit.py",
    ROOT / "restore_lcnc.py",
]


def run_ruff():
    errors = []
    try:
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "check"] + [str(p) for p in PYTHON_FILES],
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        if result.returncode != 0:
            errors.append("ruff check failed:\n" + result.stdout)
    except Exception as exc:
        errors.append("ruff unavailable: %s" % exc)
    return errors


def normalize_menu_xml(text):
    return re.sub(r"_\(", "", re.sub(r"\)_", "", text))


def parse_xml_file(path):
    raw = path.read_bytes()
    if "menu" in path.name and path.suffix == ".xml":
        text = normalize_menu_xml(raw.decode("utf-8", errors="replace"))
        return etree.fromstring(text)
    return etree.fromstring(raw)


def parse_xml_files():
    errors = []
    xml_paths = list(ROOT.glob("examples/**/*.xml"))
    xml_paths.extend(ROOT.glob("catalogs/**/*.xml"))
    for path in sorted(xml_paths):
        try:
            parse_xml_file(path)
        except Exception as exc:
            errors.append("XML parse failed %s: %s" % (path.relative_to(ROOT), exc))
    return errors


def collect_menu_cfg_paths():
    paths = set()
    for menu_xml in ROOT.glob("catalogs/**/menu*.xml"):
        root = parse_xml_file(menu_xml)
        for elem in root.iter():
            src = elem.get("src")
            if src:
                paths.add(src)
    return paths


def collect_example_cfg_paths():
    paths = set()
    for example in ROOT.glob("examples/**/*.xml"):
        root = parse_xml_file(example)
        for elem in root.iter("feature"):
            src = elem.get("src")
            if not src:
                continue
            if src.startswith("/"):
                continue
            paths.add(src)
    return paths


def check_cfg_paths():
    errors = []
    cfg_paths = collect_menu_cfg_paths() | collect_example_cfg_paths()
    for rel in sorted(cfg_paths):
        cfg_path = ROOT / "cfg" / rel
        if not cfg_path.exists():
            errors.append("missing cfg file: cfg/%s" % rel)
    return errors


def check_lathe_manifests():
    errors = []
    import lathe_polyline

    for rel in lathe_polyline.CFG_MANIFEST:
        path = ROOT / "cfg" / rel
        if not path.exists():
            errors.append("lathe CFG_MANIFEST missing: cfg/%s" % rel)

    for name in lathe_polyline.NGC_MANIFEST:
        path = ROOT / "lib" / "lathe" / name
        if not path.exists():
            errors.append("lathe NGC_MANIFEST missing: lib/lathe/%s" % name)
    return errors


def check_ngc_references_in_cfg():
    errors = []
    pattern = re.compile(r"o<([a-zA-Z0-9_]+)>")
    for cfg_path in ROOT.glob("cfg/**/*.cfg"):
        text = cfg_path.read_text(encoding="utf-8", errors="replace")
        for match in pattern.findall(text):
            if match.startswith("param_") or match.startswith("self_id"):
                continue
            ngc_candidates = [
                ROOT / "lib" / (match + ".ngc"),
                ROOT / "lib" / "lathe" / (match + ".ngc"),
                ROOT / "lib" / "mill" / (match + ".ngc"),
                ROOT / "lib" / "plasma" / (match + ".ngc"),
                ROOT / "lib" / "utilities" / (match + ".ngc"),
            ]
            if not any(p.exists() for p in ngc_candidates):
                errors.append(
                    "cfg %s references subroutine o<%s> with no matching .ngc"
                    % (cfg_path.relative_to(ROOT), match)
                )
    return errors


def check_examples_lathe_cycles():
    errors = []
    demo = ROOT / "examples" / "lathe" / "xz_profile_demo.xml"
    if not demo.exists():
        errors.append("missing examples/lathe/xz_profile_demo.xml")
        return errors

    root = parse_xml_file(demo)
    features = root.findall(".//feature")
    if not features:
        errors.append("xz_profile_demo.xml has no features")
        return errors

    profile = None
    for feature in features:
        if feature.get("src") == "lathe/xz_profile.cfg":
            profile = feature
            break
    if profile is None:
        errors.append("xz_profile_demo.xml missing lathe/xz_profile.cfg feature")
        return errors

    mode_param = None
    for param in profile.findall("param"):
        if param.get("call") == "#param_mode":
            mode_param = param
            break
    if mode_param is None:
        errors.append("xz_profile_demo.xml missing cycle type param")
    else:
        options = mode_param.get("options", "")
        for token in ("G71", "G72", "Step-down"):
            if token not in options:
                errors.append("xz_profile_demo cycle options missing %s" % token)
    return errors


def check_verify_ini_smoke():
    errors = []
    ini_template = """[DISPLAY]
DISPLAY = axis
PROGRAM_PREFIX = scripts/
SUBROUTINE_PATH = lib

[RS274NGC]
SUBROUTINE_PATH = lib
"""
    with tempfile.TemporaryDirectory() as tmp:
        ini_path = os.path.join(tmp, "test.ini")
        with open(ini_path, "w") as handle:
            handle.write(ini_template)

        if "linuxcnc" not in sys.modules:
            from unittest import mock
            sys.modules["linuxcnc"] = mock.MagicMock()

        sys.path.insert(0, str(ROOT))
        import importlib

        ncam = importlib.import_module("ncam")
        old_sys_dir = ncam.SYS_DIR
        ncam.SYS_DIR = str(ROOT)
        try:
            ncam.verify_ini(ini_path, "lathe", False)
            with open(ini_path) as handle:
                modified = handle.read()
            if "ncam.ui" not in modified:
                errors.append("verify_ini did not inject ncam.ui path")
            if "ncam/my-stuff:ncam/lib/lathe" not in modified:
                errors.append("verify_ini did not inject lathe SUBROUTINE_PATH")
            if not os.path.exists(ini_path + ".bak"):
                errors.append("verify_ini did not create .bak backup")
        except Exception as exc:
            errors.append("verify_ini smoke failed: %s" % exc)
        finally:
            ncam.SYS_DIR = old_sys_dir
    return errors


def read_ini_sections(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    normalized = []
    for line in text.splitlines():
        if line.strip() == "=":
            continue
        normalized.append(line.lstrip(" \t") + "\n")
    parser = RawConfigParser(strict=False)
    parser.read_string("".join(normalized))
    return parser


def check_sim_ini_files():
    errors = []
    for ini_path in sorted(ROOT.glob("configs/sim/**/*.ini")):
        parser = read_ini_sections(ini_path)
        try:
            display = parser.get("DISPLAY", "DISPLAY").lower()
            if display not in ("axis", "gmoccapy", "gscreen"):
                errors.append("%s has invalid DISPLAY=%s" % (ini_path.relative_to(ROOT), display))
        except Exception as exc:
            errors.append("sim ini unreadable %s: %s" % (ini_path.relative_to(ROOT), exc))
    return errors


def check_cli_help():
    errors = []
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "ncam_help_smoke.py")],
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        timeout=30,
    )
    if result.returncode != 0 or "Standalone Usage" not in result.stdout:
        errors.append("ncam help smoke failed")
    return errors


def scope_report():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~3..HEAD"],
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    modules = set()
    for rel in files:
        if rel.startswith("cfg/lathe/") or rel.startswith("lib/lathe/"):
            modules.add("lathe")
        elif rel.endswith(".py"):
            modules.add("python")
        elif rel.startswith("catalogs/"):
            modules.add("catalogs")
        elif rel.startswith("examples/"):
            modules.add("examples")
    return files, sorted(modules)


def main():
    parser = argparse.ArgumentParser(description="Validate NativeCAM project health")
    parser.add_argument("--section", choices=[
        "all", "static", "examples", "sim", "cli", "scope",
    ], default="all")
    args = parser.parse_args()

    files, modules = scope_report()
    print("Validation scope (HEAD~3..HEAD):", flush=True)
    print("  modules:", ", ".join(modules) or "none")
    print("  files:", len(files))
    if args.section == "scope":
        return 0

    checks = []
    if args.section in ("all", "static"):
        checks.extend([
            ("ruff", run_ruff),
            ("xml", parse_xml_files),
            ("cfg_paths", check_cfg_paths),
            ("lathe_manifest", check_lathe_manifests),
            ("ngc_refs", check_ngc_references_in_cfg),
        ])
    if args.section in ("all", "examples"):
        checks.append(("examples_lathe", check_examples_lathe_cycles))
    if args.section in ("all", "sim"):
        checks.extend([
            ("verify_ini", check_verify_ini_smoke),
            ("sim_ini", check_sim_ini_files),
        ])
    if args.section in ("all", "cli"):
        checks.append(("cli_help", check_cli_help))

    failed = 0
    for name, func in checks:
        errors = func()
        if errors:
            failed += len(errors)
            print("[FAIL] %s (%d issue(s))" % (name, len(errors)))
            for err in errors[:20]:
                print("  - %s" % err)
            if len(errors) > 20:
                print("  - ... %d more" % (len(errors) - 20))
        else:
            print("[OK] %s" % name)

    if failed:
        print("\nValidation failed with %d issue(s)." % failed)
        return 1
    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
