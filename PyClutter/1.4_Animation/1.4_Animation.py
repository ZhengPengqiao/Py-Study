#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter
import sys

def keyPress(self, event, _actor):
    _actor.set_position( 200,100 )
    _actor.animatev(
                     Clutter.AnimationMode.EASE_OUT_BOUNCE,
                     1500,
                     ["x"],
                     [20] )

if __name__ == '__main__':
    Clutter.init( sys.argv )

    # Create Stage
    _stage = Clutter.Stage()
    _stage.set_title( "Basic Usage" )
    _stage.set_size( 400, 200 )

    # Create Actor
    _red = Clutter.Color().new(255, 0, 0, 255) # R,G,B,alpha
    _actor = Clutter.Text().new_full(
                  "Mono 10",
                  "Hello World!",
                  _red )

    _actor.set_position( 100,100 )
    _actor_anim = _actor.animatev(
                     Clutter.AnimationMode.EASE_OUT_BOUNCE,
                     1500,
                     ["x"],
                     [20] )

    # Add Actor to the Stage
    _stage.add_actor( _actor )
    _stage.connect("destroy", lambda w: Clutter.main_quit() )
    _stage.connect('key-press-event', keyPress, _actor)

    _stage.show_all()

    Clutter.main()