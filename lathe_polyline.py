# Lathe XZ profile editor — CNC Proton extension for NativeCAM.
# Keeps bootstrap NGC variables and catalog metadata out of ncam.py.

PROFILE_DATA_ANCHOR = 70

STRATEGY_PROFILE_SHIFT = 0
STRATEGY_G71_CONTOUR = 71
STRATEGY_G72_FACE = 72
STRATEGY_G71_POCKET = 712
STRATEGY_G72_POCKET = 722
STRATEGY_G73_PATTERN = 73

CFG_MANIFEST = (
    'lathe/xz_profile.cfg',
    'lathe/xz_profile_id.cfg',
    'lathe/xz_line.cfg',
    'lathe/xz_polar.cfg',
    'lathe/xz_arc_ik.cfg',
    'lathe/xz_arc_end.cfg',
    'lathe/radius_id.cfg',
    'lathe/od_groove.cfg',
    'lathe/id_groove.cfg',
    'lathe/face_groove.cfg',
    'lathe/lathe_probe.cfg',
)

NGC_MANIFEST = (
    'poly_add_item.ngc',
    'poly_add_data.ngc',
    'poly_create.ngc',
    'poly_link.ngc',
    'poly_link_dir.ngc',
    'poly_reverse.ngc',
    'lathe_path_walk.ngc',
    'lathe_xz_move.ngc',
    'lathe_rough_step.ngc',
    'lathe_rough_step_id.ngc',
    'lathe_rough_pattern.ngc',
    'lathe_rough_pattern_id.ngc',
    'lathe_approach.ngc',
    'lathe_depart.ngc',
    'lathe_poly_create.ngc',
    'lathe_poly_add_data.ngc',
    'radius_id.ngc',
    'od_groove.ngc',
    'id_groove.ngc',
    'face_groove.ngc',
)


def _coord_aux_g(off_rot_index):
    if off_rot_index < 5:
        suffix = str(5 + off_rot_index)
    else:
        suffix = '9.' + str(off_rot_index - 4)
    return '\n#<_off_rot_coord_system>    = 5' + suffix + '\n\n'


def bootstrap_defaults(off_rot_coord_system=2):
    """NGC preamble required before any lathe XZ profile feature runs."""
    lines = [
        '#<_mill_data_start>         = %d\n' % PROFILE_DATA_ANCHOR,
        '#<in_polyline>              = 0\n',
        _coord_aux_g(off_rot_coord_system),
    ]
    return ''.join(lines)
