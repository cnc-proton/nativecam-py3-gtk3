"""Automated validation tests for NativeCAM."""

import importlib
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import lathe_polyline


def normalize_menu_xml(text):
    return re.sub(r"_\(", "", re.sub(r"\)_", "", text))


def parse_xml_file(path):
    raw = path.read_bytes()
    if "menu" in path.name and path.suffix == ".xml":
        text = normalize_menu_xml(raw.decode("utf-8", errors="replace"))
        return etree.fromstring(text)
    return etree.fromstring(raw)


PYTHON_FILES = [
    ROOT / "ncam.py",
    ROOT / "lathe_polyline.py",
    ROOT / "pref_edit.py",
    ROOT / "restore_lcnc.py",
]


def test_ruff_clean():
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check"] + [str(p) for p in PYTHON_FILES],
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    assert result.returncode == 0, result.stdout


@pytest.mark.parametrize("xml_path", sorted(ROOT.glob("examples/**/*.xml")))
def test_example_xml_parses(xml_path):
    parse_xml_file(xml_path)


@pytest.mark.parametrize("xml_path", sorted(ROOT.glob("catalogs/**/*.xml")))
def test_catalog_xml_parses(xml_path):
    parse_xml_file(xml_path)


def test_lathe_manifest_files_exist():
    for rel in lathe_polyline.CFG_MANIFEST:
        assert (ROOT / "cfg" / rel).exists(), rel
    for name in lathe_polyline.NGC_MANIFEST:
        assert (ROOT / "lib" / "lathe" / name).exists(), name


def test_bootstrap_defaults_contains_anchor_and_coord_system():
    text = lathe_polyline.bootstrap_defaults(off_rot_coord_system=2)
    assert "#<_mill_data_start>" in text
    assert str(lathe_polyline.PROFILE_DATA_ANCHOR) in text
    assert "#<_off_rot_coord_system>" in text
    assert "#<in_polyline>" in text


def test_bootstrap_defaults_coord_system_variants():
    for index in (0, 2, 6):
        text = lathe_polyline.bootstrap_defaults(off_rot_coord_system=index)
        assert "#<_off_rot_coord_system>" in text


def test_xz_profile_demo_has_lathe_profile():
    demo = ROOT / "examples" / "lathe" / "xz_profile_demo.xml"
    root = parse_xml_file(demo)
    srcs = {feature.get("src") for feature in root.findall(".//feature")}
    assert "lathe/xz_profile.cfg" in srcs
    assert "lathe/material.cfg" in srcs


def test_xz_profile_cfg_cycle_options_include_g73():
    cfg = (ROOT / "cfg" / "lathe" / "xz_profile.cfg").read_text(encoding="utf-8")
    for token in ("G71", "G72", "G73", "712", "722"):
        assert token in cfg


def test_verify_ini_creates_backup_and_injects_nativecam(tmp_path, monkeypatch):
    ini_path = tmp_path / "axis-lathe.ini"
    ini_path.write_text(
        "[DISPLAY]\n"
        "DISPLAY = axis\n"
        "PROGRAM_PREFIX = scripts/\n"
        "\n"
        "[RS274NGC]\n"
        "SUBROUTINE_PATH = lib\n",
        encoding="utf-8",
    )

    ncam = importlib.import_module("ncam")
    monkeypatch.setattr(ncam, "SYS_DIR", str(ROOT))

    ncam.verify_ini(str(ini_path), "lathe", False)
    modified = ini_path.read_text(encoding="utf-8")

    assert (tmp_path / "axis-lathe.ini.bak").exists()
    assert "ncam.ui" in modified
    assert "ncam/my-stuff:ncam/lib/lathe" in modified
    assert "EMBED_TAB_NAME = NativeCAM" not in modified
    assert "GLADEVCP" in modified


def test_verify_ini_tab_mode_for_gmoccapy(tmp_path, monkeypatch):
    ini_path = tmp_path / "gmoccapy.ini"
    ini_path.write_text(
        "[DISPLAY]\n"
        "DISPLAY = gmoccapy\n"
        "\n"
        "[RS274NGC]\n"
        "SUBROUTINE_PATH = lib\n",
        encoding="utf-8",
    )

    ncam = importlib.import_module("ncam")
    monkeypatch.setattr(ncam, "SYS_DIR", str(ROOT))
    ncam.verify_ini(str(ini_path), "mill", True)

    modified = ini_path.read_text(encoding="utf-8")
    assert "EMBED_TAB_NAME = NativeCAM" in modified
    assert "--catalog=mill" in modified


def test_example_feature_cfg_files_exist():
    missing = []
    for example in ROOT.glob("examples/**/*.xml"):
        root = parse_xml_file(example)
        for feature in root.iter("feature"):
            src = feature.get("src")
            if not src or src.startswith("/"):
                continue
            if not (ROOT / "cfg" / src).exists():
                missing.append("%s -> %s" % (example.relative_to(ROOT), src))
    assert not missing, "missing cfg files:\n" + "\n".join(missing)


def test_menu_cfg_files_exist():
    missing = []
    for menu_xml in ROOT.glob("catalogs/**/menu*.xml"):
        root = parse_xml_file(menu_xml)
        for elem in root.iter():
            src = elem.get("src")
            if src and not (ROOT / "cfg" / src).exists():
                missing.append("%s -> %s" % (menu_xml.relative_to(ROOT), src))
    assert not missing, "missing menu cfg files:\n" + "\n".join(missing)


def test_sim_ini_files_have_valid_display():
    from scripts.validate_project import read_ini_sections

    for ini_path in sorted(ROOT.glob("configs/sim/**/*.ini")):
        parser = read_ini_sections(ini_path)
        display = parser.get("DISPLAY", "DISPLAY").lower()
        assert display in ("axis", "gmoccapy", "gscreen"), ini_path


def test_lathe_ngc_calls_in_xz_profile_cfg_exist():
    cfg = (ROOT / "cfg" / "lathe" / "xz_profile.cfg").read_text(encoding="utf-8")
    calls = set(re.findall(r"o<([a-zA-Z0-9_]+)>", cfg))
    expected = {
        "lathe_path_walk",
        "poly_add_item",
        "lathe_poly_create",
        "lathe_rough_step",
        "lathe_rough_pattern",
        "get_max",
    }
    for name in expected:
        assert name in calls
        ngc = ROOT / "lib" / "lathe" / (name + ".ngc")
        util = ROOT / "lib" / "utilities" / (name + ".ngc")
        assert ngc.exists() or util.exists(), name
