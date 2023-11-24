# main.py
#
# Copyright 2023 André de Campos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import EasyfreezeWindow


class EasyfreezeApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='Andr.EasyFreeze.app',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)
        self.create_action("freeze", self.on_freeze_action)

    def do_activate(self):
        """Called when the application is activated.

        Raise the application's main window, creating it if necessary.
        """
        win = self.props.active_window
        if not win:
            win = EasyfreezeWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='easyfreeze',
                                application_icon='Andr.EasyFreeze.app',
                                developer_name='André de Campos',
                                version='0.1.0',
                                developers=['André de Campos'],
                                copyright='© 2023 André de CamposS')
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


    def on_freeze_action(self, button):
        dialog = Adw.MessageDialog(body="Sistema Congelado")

        dialog.add_response("ok", "Ok")
        dialog.connect("response", dialog_response)
        dialog.present()

    def descongelar(self, widget):
        dialog = Adw.MessageDialog(body="Sistema Descongelado")


        dialog.add_response("ok", "Ok")

        dialog.connect("response", dialog_response)
        dialog.present()

    def dialog_response(dialog: Adw.MessageDialog, response: str):
        print(response)
        dialog.close()

def main(version):
    """The application's entry point."""
    app = EasyfreezeApplication()
    return app.run(sys.argv)


