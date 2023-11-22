#!/usr/bin/python

import subprocess
import os
import gi

os.environ["PATH"] = "/usr/local/bin"

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
import workbench


def congelar(_widget):
    dialog = Adw.MessageDialog(body="Sistema Congelado", transient_for=workbench.window)

    dialog.add_response("ok", "Ok")
    dialog.connect("response", dialog_response)
    dialog.present()


def descongelar(_widget):
    dialog = Adw.MessageDialog(
        body="Sistema Descongelado", transient_for=workbench.window
    )

    command = "apt update"

    try:
        # This will prompt the user for the sudo password
        result = subprocess.run(
            ["sudo", command],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running sudo command: {e}")
        print(f"Error output: {e.stderr}")

    dialog.add_response("ok", "Ok")

    dialog.connect("response", dialog_response)
    dialog.present()


def dialog_response(dialog: Adw.MessageDialog, response: str):
    print(response)
    dialog.close()


button_box: Gtk.Box = workbench.builder.get_object("buttons")

congela = Gtk.Button(
    label="Congelar sistema", margin_top=6, css_classes=["suggested-action"]
)
congela.connect("clicked", congelar)

descongela = Gtk.Button(
    label="Descongelar sistema", margin_top=6, css_classes=["suggested-action"]
)
descongela.connect("clicked", descongelar)

button_box.append(congela)
button_box.append(descongela)

print("TOP")

