#!/usr/bin/python3
# -*- coding:utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.set_default_size(300,200)
window.set_title("Hello World in PyGTK")
window.connect("destroy", Gtk.main_quit)
label = Gtk.Label("Hello World")

window.add(label)
window.show_all()
Gtk.main()