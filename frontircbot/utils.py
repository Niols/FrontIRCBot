#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import defaults as DEFAULT



def parse_server(server, as_string=False):
    """
    Returns a (server, port) tuple filled with informations taken from the
    *server* argument. If *as_string* is set to True, returns a `server:port`
    string instead.
    """
    
    if as_string:
        return '%s:%d' % parse_server(server)

    if not isinstance(server, (list, tuple)):
        return parse_server(server.split(':'))
        
    if   len(server) == 1: return (server[0], DEFAULT.PORT)
    elif len(server) == 2: return (server[0], int(server[1]))
    else:
        raise Exception('parse_server: Didn\'t know what to do with `%s`.' %
                        str(server))


    
