# NativeCAM for LinuxCNC (Python 3 & Gtk3 Port)

This is a ported version of **NativeCAM** for LinuxCNC, migrated from Python 2.7 / Gtk2 to **Python 3** and **Gtk3**. It is specifically designed for compatibility with modern distributions like **Debian 12 Bookworm** and **LinuxCNC 2.9+**.

## Key Changes in this Port
* **Python 3 Migration**: Fully updated codebase to run on modern Python interpreters.
* **Gtk3 Integration**: UI migrated to Gtk3 for better rendering and system compatibility.
* **Debian Bookworm Ready**: Tested and optimized for the latest stable LinuxCNC environments.

## Installation
If you are using the provided `.deb` package:
1. Download the latest release from the [Releases](https://github.com/cnc-proton/nativecam-py3-gtk3/releases) page.
2. Install it using:
   ```bash
   sudo apt install ./nativecam_py3.deb
