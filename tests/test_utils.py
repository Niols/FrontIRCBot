#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from nose.tools import assert_raises

from frontircbot.utils import *
from frontircbot.defaults import PORT as DEFAULT_PORT



def test_parse_server():

    assert parse_server('irc.server.net') == ('irc.server.net', DEFAULT_PORT)
    assert parse_server(('irc.server.net',)) == ('irc.server.net', DEFAULT_PORT)
    assert parse_server(['irc.server.net',]) == ('irc.server.net', DEFAULT_PORT)

    assert parse_server('irc.server.net:1234') == ('irc.server.net', 1234)
    assert parse_server(('irc.server.net',1234)) == ('irc.server.net', 1234)
    assert parse_server(('irc.server.net','1234')) == ('irc.server.net', 1234)
    assert parse_server(['irc.server.net',1234]) == ('irc.server.net', 1234)
    assert parse_server(['irc.server.net','1234']) == ('irc.server.net', 1234)

    assert_raises(ParseError, parse_server, 'irc.server.net:-1234')
    assert_raises(ParseError, parse_server, ('irc.server.net', -1234))
    assert_raises(ParseError, parse_server, ('irc.server.net', '-1234'))

    assert_raises(ParseError, parse_server, 'irc.server.net:invalid')
    assert_raises(ParseError, parse_server, ('irc.server.net', 'invalid'))

    # weird cases. you shouldn't even write that
    assert parse_server(('irc.server.net:1234',)) == ('irc.server.net:1234', DEFAULT_PORT)
    assert parse_server(('irc.server.net:-1234',)) == ('irc.server.net:-1234', DEFAULT_PORT)
    assert parse_server(('irc.server.net:invalid',)) == ('irc.server.net:invalid', DEFAULT_PORT)

    assert_raises(ParseError, parse_server, 'irc.server.net:6667:foo')
    assert_raises(ParseError, parse_server, ('irc.server.net', '6667', 'foo'))
    assert_raises(ParseError, parse_server, ['irc.server.net', '6667', 'foo'])
