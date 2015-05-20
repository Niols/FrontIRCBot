#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import defaults as DEFAULT



class ParseError(Exception): pass

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
        
    if len(server) == 1:
        return (server[0], DEFAULT.PORT)

    elif len(server) == 2:
        try:
            port = int(server[1])
        except ValueError:
            raise ParseError('Port must be a positive integer. Received `%s`' % server[1])
        if port > 0:
            return (server[0], port)
        else:
            raise ParseError('Port must be a positive integer. Received `%d`' % port)

    else:
        raise ParseError('Don\'t know what to do with `%s`' % str(server))

    
