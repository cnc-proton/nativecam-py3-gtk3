"""GTK3 stylesheet for ProtonCAM.

LinuxCNC GladeVCP still embeds GTK3 (XEMBED). This is a visual refresh,
not a GTK4 rewrite — Qt/Qtvcp is the planned second backend.
"""

import os

CSS = b"""
/* ProtonCAM — GTK3 application theme */
.protoncam-panel, .protoncam-panel * {
}

treeview {
    font-size: 11pt;
}

treeview:selected {
    background-color: #2b6cb0;
    color: #ffffff;
}

toolbar {
    padding: 4px;
    background-color: #f4f6f8;
}

button {
    padding: 4px 8px;
}

dialog {
    background-color: #fafafa;
}

entry, spinbutton {
    min-height: 1.6em;
}

paned separator {
    background-color: #cbd5e0;
    min-width: 6px;
    min-height: 6px;
}
"""


def apply_gtk3_theme(gtk_module=None, gdk_module=None, css_path=None):
    """Load application CSS. No-op if GTK is unavailable (tests, headless)."""
    try:
        if gtk_module is None:
            import gi
            gi.require_version('Gtk', '3.0')
            from gi.repository import Gtk as gtk_module
            from gi.repository import Gdk as gdk_module
        provider = gtk_module.CssProvider()
        if css_path and os.path.isfile(css_path):
            provider.load_from_path(css_path)
        else:
            provider.load_from_data(CSS)
        screen = gdk_module.Screen.get_default()
        if screen is None:
            return False
        gtk_module.StyleContext.add_provider_for_screen(
            screen, provider, gtk_module.STYLE_PROVIDER_PRIORITY_APPLICATION)
        return True
    except Exception:
        return False
