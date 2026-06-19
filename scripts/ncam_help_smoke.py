#!/usr/bin/env python3
"""CLI smoke test for ncam.py without requiring LinuxCNC."""

import os
import runpy
import sys
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.chdir(ROOT)
sys.modules["linuxcnc"] = mock.MagicMock()
sys.argv = ["ncam.py", "-h"]
runpy.run_path(os.path.join(ROOT, "ncam.py"), run_name="__main__")
