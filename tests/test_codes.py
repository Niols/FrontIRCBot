#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from frontircbot.codes import *



def dir_attr(c):
    return [a for a in dir(c) if a[0] != '_']


def test_ColorCode():
    assert hasattr(ColorCode, 'Red')
    assert hasattr(ColorCode, 'Blue')
    assert hasattr(ColorCode, 'Green')
    assert hasattr(ColorCode, 'Yellow')
    assert hasattr(ColorCode, 'Pink')
    assert hasattr(ColorCode, 'Gray')
    assert len(dir_attr(ColorCode)) == 16

def test_Color():
    assert dir_attr(Color) == dir_attr(ColorCode)
    for color in dir_attr(ColorCode):
        assert hasattr(Color, color)
        assert getattr(Color, color) == '%c%d' % (ControlCode.Color, getattr(ColorCode, color))
    assert not hasattr(Color, 'invalid')

def test_ControlCode():
    assert hasattr(ControlCode, 'Color')
    assert hasattr(ControlCode, 'Bold')
    assert hasattr(ControlCode, 'Underline')
    assert hasattr(ControlCode, 'Reverse')
    assert hasattr(ControlCode, 'Reset')

def test_Control():
    assert dir_attr(Control) == dir_attr(ControlCode)
    for control in dir_attr(ControlCode):
        assert hasattr(Control, control)
        assert getattr(Control, control) == '%c' % (getattr(ControlCode, control),)
    assert not hasattr(Control, 'invalid')
