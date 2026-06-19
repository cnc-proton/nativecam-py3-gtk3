"""Pytest fixtures shared across NativeCAM validation tests."""

import sys
from unittest import mock

# ncam.py imports linuxcnc at module load and calls err_exit() (GTK dialog) on failure.
if "linuxcnc" not in sys.modules:
    sys.modules["linuxcnc"] = mock.MagicMock()
