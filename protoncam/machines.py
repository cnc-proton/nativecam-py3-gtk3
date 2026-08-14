"""Machine families ProtonCAM can target.

Catalog names are directories under catalogs/. Keep mill/plasma/lathe
working; mill4, mill5, millturn and universal are the structured split.
"""

from collections import namedtuple

Machine = namedtuple('Machine', [
    'catalog',
    'title',
    'axes',
    'family',
    'status',
    'notes',
])

MACHINES = (
    Machine('mill', '3-axis mill', 'XYZ', 'mill',
            'stable', 'Original NativeCAM mill catalog plus Side Drill.'),
    Machine('mill4', '4-axis mill', 'XYZA', 'mill',
            'indexing', 'Rotary A (or B) indexing around the mill catalog.'),
    Machine('mill5', '5-axis mill', 'XYZAB', 'mill',
            'setup', 'Dual rotary + optional G43.4 TCP; simultaneous CAM later.'),
    Machine('lathe', '2-axis lathe', 'XZ', 'lathe',
            'stable', 'Facing, turning, threading, XZ profile (G71/G72).'),
    Machine('millturn', 'Mill-turn / live tooling', 'XZC', 'millturn',
            'setup', 'Lathe ops plus live-tool mill/drill from C or the spindle.'),
    Machine('plasma', 'Plasma cutter', 'XY', 'plasma',
            'stable', 'Original NativeCAM plasma catalog.'),
    Machine('universal', 'Universal mill + lathe', 'XYZAB C', 'universal',
            'setup', 'One UI for mill, rotary and turning on a mixed machine.'),
)

DEFAULT_CATALOG = 'mill'
VALID_CATALOGS = [m.catalog for m in MACHINES]
_BY_NAME = {m.catalog: m for m in MACHINES}


def get_machine(catalog):
    return _BY_NAME.get(catalog)


def list_machines():
    return MACHINES


def catalog_from_embed_command(val):
    """Pick catalog from a GLADEVCP / EMBED_TAB_COMMAND string."""
    if not val:
        return None
    text = val.lower()
    # Longer names first so 'mill4' is not swallowed by 'mill'
    for name in ('millturn', 'universal', 'mill5', 'mill4', 'plasma', 'lathe', 'mill'):
        if name in text:
            return name
    return None
