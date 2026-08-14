"""Canonical product identity and copyright notices.

GPL-2 requires these notices to stay intact when the work is distributed.
Do not replace CNC Proton or Fernand Veilleux with a fork maintainer.
"""

PRODUCT_NAME = 'ProtonCAM'
PRODUCT_TAGLINE = 'Conversational CAM for LinuxCNC'
LINEAGE = 'Based on NativeCAM by Fernand Veilleux (FernV)'

APP_VERSION = '3.0a'

APP_COPYRIGHT = '''Copyright © 2017 Fernand Veilleux : fernveilleux@gmail.com
Copyright © 2012 Nick Drobchenko aka Nick from cnc-club.ru
Copyright © 2026 CNC Proton (Python 3 / GTK3 port, Side Drill, ProtonCAM)'''

APP_AUTHORS = [
    'Fernand Veilleux (original NativeCAM author)',
    'Nick Drobchenko (initiator)',
    'Meison Kim',
    'Alexander Wigen',
    'Konstantin Navrockiy',
    'Mit Zot',
    'Dewey Garrett',
    'Karl Jacobs',
    'Philip Mullen',
    'CNC Proton (Python 3 / GTK3 port, Side Drill, ProtonCAM)',
]

APP_TITLE = 'ProtonCAM for LinuxCNC'
APP_COMMENTS = (
    'Conversational CAM for mill, lathe, plasma, 4/5-axis and mill-turn. '
    'Official Python 3 / GTK3 line by CNC Proton, based on NativeCAM (FernV).'
)

HOME_PAGE = 'https://github.com/cnc-proton/nativecam-py3-gtk3'
DONATE_URL = 'https://github.com/sponsors/cnc-proton'
GITHUB_LABEL = 'cnc-proton/nativecam-py3-gtk3'

# gettext domain stays nativecam so existing .mo files still apply
GETTEXT_DOMAIN = 'nativecam'


def copyright_ok():
    """True when required copyright holders are present."""
    text = APP_COPYRIGHT + '\n' + ' '.join(APP_AUTHORS)
    return (
        'Fernand Veilleux' in text
        and 'CNC Proton' in text
        and 'greatEndian' not in text
    )
