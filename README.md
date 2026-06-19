# NativeCAM for LinuxCNC (Python 3 & GTK3 Port)

This is a ported version of **NativeCAM** for LinuxCNC, migrated from
Python 2.7 / GTK2 to **Python 3** and **GTK3**. Designed for compatibility
with **Debian 13 Trixie** and **LinuxCNC 2.9+**.

## Key Changes in this Port

- **Python 3 Migration** — fully updated codebase for modern Python interpreters
- **GTK3 Integration** — UI migrated from GTK2 for better rendering and compatibility
- **Horizontal Side Drilling** — new Side Drill feature for multi-spindle machines (Top / Bottom / Left / Right)
- **Horizontal Tool Visualization** — correct tool orientation display in AXIS for side spindles
- **Phantom Window Fix** — GTK popup windows are properly closed when LinuxCNC exits
- **Debian 13 Trixie Ready** — tested with LinuxCNC 2.9 on Debian 13

## Installation

1. Download the latest release from the [Releases](https://github.com/cnc-proton/nativecam-py3-gtk3/releases) page.
2. Install it using:

```bash
sudo apt install ./nativecam_2.0b-4_all.deb
```

## Usage

Run `ncam -h` for help and all command line options.

### 1. Stand-alone mode

```bash
ncam
```

Creates and uses the `~/nativecam` directory. Requires correct
`SUBROUTINE_PATH` in your LinuxCNC INI file to be fully functional.

### 2. Embedded mode

Use with any of the supplied examples from the LinuxCNC Configuration Selector,
or embed into your own INI file:

```bash
# Run in the directory containing your .ini file:
ncam -i inifilename -c mill   # or: plasma | lathe
```

This will create a backup and automatically modify your INI file.
Then start LinuxCNC normally:

```bash
linuxcnc inifilename
```

## Tutorials

- [NativeCAM on YouTube](https://www.youtube.com/channel/UCjOe4VxKL86HyVrshTmiUBQ)
- [LinuxCNC Forum Thread](https://forum.linuxcnc.org/forum/40-subroutines-and-ngcgui)

## Credits

**Original NativeCAM** — [Fernand Veilleux (FernV)](https://github.com/FernV/NativeCAM)  
Based on work by Nick Drobchenko and the LinuxCNC community.

**Python 3 / GTK3 port (2026)** — [CNC Proton](https://github.com/cnc-proton)  
This repository is an independent port of NativeCAM from Python 2.7 / PyGTK / GTK2
to Python 3 / PyGObject / GTK3. The migration covered the full application stack
(`ncam.py`, Glade UI, preferences, GladeVCP embedding, Debian packaging) and added
Side Drill, workpiece-based milling references, and LinuxCNC 2.9 / Debian 13 support.

See [AUTHORS](AUTHORS) for the complete attribution list.

### Attribution for derivative works

This project is licensed under GPL-2. Forks and derivatives may modify and
redistribute the code, but must **retain all copyright notices**, including
the CNC Proton port credit, and remain under GPL-2. Removing port attribution
while using this codebase is discouraged and may misrepresent the origin of
the Python 3 / GTK3 work.
