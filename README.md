# ProtonCAM for LinuxCNC

Official conversational CAM line by **CNC Proton**.

ProtonCAM is the Python 3 / GTK3 continuation of NativeCAM
([Fernand Veilleux / FernV](https://github.com/FernV/NativeCAM)).
The running application, Debian package path, and `ncam` command stay
compatible with LinuxCNC GladeVCP. The product name in the UI is **ProtonCAM**.

**Official repository:** https://github.com/cnc-proton/nativecam-py3-gtk3

## Lineage (GPL-2)

- Original NativeCAM: **Fernand Veilleux (FernV)**
- LinuxCNC-Features basis: **Nick Drobchenko** and contributors
- Python 3 / GTK3 port, Side Drill, ProtonCAM: **CNC Proton**

These copyright notices must stay in the source when the work is copied
or forked.

## Machine catalogs

| Catalog | Machine | Status |
|---------|---------|--------|
| `mill` | 3-axis mill | stable |
| `mill4` | 4-axis mill (A/B indexing) | indexing |
| `mill5` | 5-axis mill (dual rotary, optional G43.4) | setup |
| `lathe` | 2-axis lathe + XZ profile | stable |
| `millturn` | mill-turn / live tooling | setup |
| `plasma` | plasma | stable |
| `universal` | mill + turning + rotary | setup |

```bash
ncam -c mill
ncam -c mill4
ncam -c mill5
ncam -c lathe
ncam -c millturn
ncam -c universal
python3 -m protoncam    # identity + machine list
```

Simultaneous 5-axis toolpaths are **not** generated yet. `mill5` sets
kinematics and optional TCP (`G43.4`); use Index A/B for rotary work.

## Layout

```
protoncam/          product identity, machine families, GTK3 theme
ncam.py             LinuxCNC-embedded UI (GladeVCP / GTK3)
catalogs/           per-machine menus (mill, mill4, mill5, lathe, …)
cfg/  lib/          features and NGC subroutines
graphics/protoncam.css
```

GTK3 remains the embed path (AXIS / gmoccapy XEMBED). The CSS theme is
the first UI refresh; a Qt/Qtvcp backend is the next GUI step.

## Installation

1. Download the latest release from
   [Releases](https://github.com/cnc-proton/nativecam-py3-gtk3/releases).
2. Install:

```bash
sudo apt install ./nativecam_2.0b-5_all.deb
```

Package name stays `nativecam` so LinuxCNC auxiliary paths keep working.

## Credits

Original NativeCAM developed by
[Fernand Veilleux (FernV)](https://github.com/FernV/NativeCAM).  
Python 3 / GTK3 port, Side Drill, and ProtonCAM by **CNC Proton**.
