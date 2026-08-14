import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from protoncam.identity import APP_AUTHORS, APP_COPYRIGHT, PRODUCT_NAME, copyright_ok
from protoncam.machines import (
    VALID_CATALOGS,
    catalog_from_embed_command,
    get_machine,
    list_machines,
)


class IdentityTests(unittest.TestCase):
    def test_product_name(self):
        self.assertEqual(PRODUCT_NAME, 'ProtonCAM')

    def test_gpl_notices_intact(self):
        self.assertTrue(copyright_ok())
        self.assertIn('Fernand Veilleux', APP_COPYRIGHT)
        self.assertIn('CNC Proton', APP_COPYRIGHT)
        self.assertNotIn('greatEndian', APP_COPYRIGHT)
        self.assertTrue(any('CNC Proton' in a for a in APP_AUTHORS))


class MachineTests(unittest.TestCase):
    def test_catalogs_cover_families(self):
        names = set(VALID_CATALOGS)
        for required in ('mill', 'mill4', 'mill5', 'lathe', 'millturn',
                         'plasma', 'universal'):
            self.assertIn(required, names)

    def test_embed_command_prefers_longer_names(self):
        self.assertEqual(catalog_from_embed_command('ncam.py -c mill4'), 'mill4')
        self.assertEqual(catalog_from_embed_command('ncam.py -c mill5'), 'mill5')
        self.assertEqual(catalog_from_embed_command('ncam.py -c millturn'), 'millturn')
        self.assertEqual(catalog_from_embed_command('ncam.py -c mill'), 'mill')
        self.assertEqual(catalog_from_embed_command('ncam.py -c lathe'), 'lathe')

    def test_axes(self):
        self.assertEqual(get_machine('mill').axes, 'XYZ')
        self.assertEqual(get_machine('mill4').axes, 'XYZA')
        self.assertEqual(get_machine('mill5').axes, 'XYZAB')
        self.assertEqual(get_machine('lathe').axes, 'XZ')

    def test_catalog_menus_exist(self):
        for m in list_machines():
            menu = os.path.join(ROOT, 'catalogs', m.catalog, 'menu.xml')
            self.assertTrue(os.path.isfile(menu), menu)


class FeatureFileTests(unittest.TestCase):
    def test_new_cfg_files(self):
        for rel in (
            'cfg/mill/index-axisB.cfg',
            'cfg/mill/kinematics-4axis.cfg',
            'cfg/mill/kinematics-5axis.cfg',
            'cfg/lathe/live-tool.cfg',
            'cfg/mill/drill-side.cfg',
        ):
            path = os.path.join(ROOT, rel)
            self.assertTrue(os.path.isfile(path), path)


if __name__ == '__main__':
    unittest.main()
