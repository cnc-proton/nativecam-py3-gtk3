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
sudo apt install ./nativecam_2.0b_all.deb
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

Original NativeCAM developed by [Fernand Veilleux (FernV)](https://github.com/FernV/NativeCAM).  
Python 3 / GTK3 migration and Side Drill feature maintained by CNC Proton.
