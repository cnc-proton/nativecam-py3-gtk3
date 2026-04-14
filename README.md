# NativeCAM for LinuxCNC (Python 3 & Gtk3 Port)

This is a ported version of **NativeCAM** for LinuxCNC, migrated from Python 2.7 / Gtk2 to **Python 3** and **Gtk3**. It is specifically designed for compatibility with modern distributions like **Debian 13 Bookworm** and **LinuxCNC 2.9+**.

## Key Changes in this Port
* **Python 3 Migration**: Fully updated codebase to run on modern Python interpreters.
* **Gtk3 Integration**: UI migrated to Gtk3 for better rendering and system compatibility.
* **Debian Bookworm Ready**: Tested and optimized for the latest stable LinuxCNC environments.

## Installation
If you are using the provided `.deb` package:
1. Download the latest release from the [Releases](https://github.com/cnc-proton/nativecam-py3-gtk3/releases) page.
2. Install it using:
   ```bash
   sudo apt install ./nativecam_2.0b_all.deb
Usage

Type ncam -h for help and command line options.
1. Stand-alone mode

Using the command ncam will create and use the ~/nativecam directory and copy support files and links in the sub-directory ncam. Note: It requires the correct SUBROUTINE_PATH in LinuxCNC to be fully functional.
2. Embedded mode

    Use with any of the supplied examples from the LinuxCNC Configuration Selector.

    To use with your own .ini file:

        Open a terminal in the directory containing your .ini file.

        Run: ncam -i(inifilename) -c('mill' | 'plasma' | 'lathe').

        This will automatically create a backup and modify your file for embedding.

    Start LinuxCNC normally: linuxcnc inifilename.

Tutorials

    YouTube Channel: NativeCAM on YouTube.

    Forum Discussion: LinuxCNC Forum Thread.

Credits

Original NativeCAM was developed by FernV. This Python 3 / Gtk3 migration is maintained by CNC Proton.
