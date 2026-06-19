"""Lightweight stress checks that do not require a full GTK session."""

import importlib
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tests.test_validation import parse_xml_file


def _load_ncam_module():
    return importlib.import_module("ncam")


@pytest.fixture
def ncam_module():
    return _load_ncam_module()


def test_verify_ini_idempotent_on_second_run(tmp_path, ncam_module, monkeypatch):
    monkeypatch.setattr(ncam_module, "SYS_DIR", str(ROOT))
    ini_path = tmp_path / "repeat.ini"
    ini_path.write_text(
        "[DISPLAY]\nDISPLAY = axis\n\n[RS274NGC]\nSUBROUTINE_PATH = lib\n",
        encoding="utf-8",
    )

    ncam_module.verify_ini(str(ini_path), "lathe", False)
    first = ini_path.read_text(encoding="utf-8")
    ncam_module.verify_ini(str(ini_path), "lathe", False)
    second = ini_path.read_text(encoding="utf-8")
    assert first == second


@pytest.mark.parametrize("catalog", ["mill", "lathe", "plasma"])
def test_verify_ini_all_catalogs(tmp_path, ncam_module, monkeypatch, catalog):
    monkeypatch.setattr(ncam_module, "SYS_DIR", str(ROOT))
    ini_path = tmp_path / ("%s.ini" % catalog)
    ini_path.write_text(
        "[DISPLAY]\nDISPLAY = gscreen\n\n[RS274NGC]\nSUBROUTINE_PATH = lib\n",
        encoding="utf-8",
    )
    ncam_module.verify_ini(str(ini_path), catalog, False)
    modified = ini_path.read_text(encoding="utf-8")
    assert "ncam/lib/%s" % catalog in modified


def test_reparse_all_examples_many_times():
    examples = sorted(ROOT.glob("examples/**/*.xml"))
    for _ in range(25):
        for path in examples:
            parse_xml_file(path)


def test_bootstrap_defaults_repeated_generation():
    import lathe_polyline

    outputs = {lathe_polyline.bootstrap_defaults(i) for i in range(10)}
    assert len(outputs) == 10


def test_ncam_help_repeated_invocation():
    for _ in range(10):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "ncam_help_smoke.py")],
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            timeout=30,
        )
        assert result.returncode == 0
        assert "Standalone Usage" in result.stdout
