# ProtonCAM — conversational CAM for LinuxCNC.
# Copyright © 2017 Fernand Veilleux (NativeCAM)
# Copyright © 2026 CNC Proton (Python 3 / GTK3 port, ProtonCAM)

from protoncam.identity import (
    APP_AUTHORS,
    APP_COMMENTS,
    APP_COPYRIGHT,
    APP_VERSION,
    DONATE_URL,
    HOME_PAGE,
    PRODUCT_NAME,
    PRODUCT_TAGLINE,
)
from protoncam.machines import DEFAULT_CATALOG, VALID_CATALOGS, get_machine, list_machines

__all__ = [
    'APP_AUTHORS',
    'APP_COMMENTS',
    'APP_COPYRIGHT',
    'APP_VERSION',
    'DEFAULT_CATALOG',
    'DONATE_URL',
    'HOME_PAGE',
    'PRODUCT_NAME',
    'PRODUCT_TAGLINE',
    'VALID_CATALOGS',
    'get_machine',
    'list_machines',
]
