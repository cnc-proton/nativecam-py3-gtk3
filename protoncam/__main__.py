"""python3 -m protoncam — identity and machine list."""

from protoncam.identity import (
    APP_COPYRIGHT,
    APP_VERSION,
    HOME_PAGE,
    PRODUCT_NAME,
    PRODUCT_TAGLINE,
    copyright_ok,
)
from protoncam.machines import list_machines


def main():
    print('%s %s' % (PRODUCT_NAME, APP_VERSION))
    print(PRODUCT_TAGLINE)
    print(HOME_PAGE)
    print()
    print(APP_COPYRIGHT)
    print()
    print('Machines:')
    for m in list_machines():
        print('  %-12s  %-28s  %-10s  [%s]' % (
            m.catalog, m.title, m.axes, m.status))
        print('               %s' % m.notes)
    if not copyright_ok():
        raise SystemExit('error: copyright notices were altered')


if __name__ == '__main__':
    main()
