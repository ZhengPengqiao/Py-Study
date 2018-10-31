#!/usr/bin/python3
#! -*- coding: utf-8 -*-
import gi
gi.require_version('Clutter', '1.0')

from gi.repository import Clutter
import sys

if __name__ == '__main__':
    Clutter.init(sys.argv)

    _script = Clutter.Script()
    _script.load_from_file( "ui.json")
    stage = _script.get_object("stage")
    _script.connect_signals( stage )
    stage.connect("destroy", lambda w: Clutter.main_quit() )

    stage.show_all()
    Clutter.main()