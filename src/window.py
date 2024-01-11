# window.py
#
# Copyright 2024 André de Campos, Jaasiel Abner Alves Sousa
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

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio


@Gtk.Template(resource_path='/com/app/easyfreeze/window.ui')
class EasyfreezeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'EasyfreezeWindow'

    main_screen = Gtk.Template.Child()
    freeze_button = Gtk.Template.Child()
    melt_button = Gtk.Template.Child()
    update_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_resizable(False)

        freeze_action = Gio.SimpleAction(name="freeze")
        freeze_action.connect("activate", self.freeze_action)
        self.freeze_button.connect("clicked", lambda button: freeze_action.activate(None))

        melt_action = Gio.SimpleAction(name="melt")
        melt_action.connect("activate", self.melt_action)
        self.melt_button.connect("clicked", lambda button: melt_action.activate(None))

        update_action = Gio.SimpleAction(name="update")
        update_action.connect("activate", self.update_action)
        self.update_button.connect("clicked", lambda button: update_action.activate(None))

    def freeze_action(self, action, parameter):
        print("Que frio do caralho")

    def melt_action(self, action, parameter):
        print("CalorCalor")

    def update_action(self, action, parameter):
        print("Atualizadoooooooo")


