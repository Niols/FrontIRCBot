#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import irc.client
import threading

import defaults as DEFAULT
import utils

IS_PY2 = sys.version[0] == '2'
if IS_PY2:
    import Queue as queue
else:
    import queue



class _SingleServer_FrontIRCBot(irc.client.SimpleIRCClient):

    def __init__(self, server, nickname, message_queues):
        irc.client.SimpleIRCClient.__init__(self)
        self.server = server
        self.channels = []
        self.nickname = nickname
        self.message_queues = message_queues

    def on_welcome(self, connection, event):
        connection.execute_every(DEFAULT.TIME_BETWEEN_MESSAGES, self.privmsg_loop)

    def privmsg_loop(self):
        for target in self.message_queues:
            if irc.client.is_channel(target) and target not in self.channels:
                self.connection.join(target)
                self.channels.append(target)
            try:
                self.connection.privmsg(target, self.message_queues[target].get_nowait())
            except queue.Empty:
                pass

    def is_on_channel(self, channel):
        return channel in self.channels


    
class _SingleServer_FrontIRCBot_Thread(threading.Thread):

    def __init__(self, server, nickname, message_queues):
        threading.Thread.__init__(self)
        self.server = utils.parse_server(server)
        self.nickname = nickname
        self.message_queues = message_queues
    
    def run(self):
        self.bot = _SingleServer_FrontIRCBot(self.server, self.nickname, self.message_queues)
        try:
            self.bot.connect(self.server[0], self.server[1], self.nickname)
        except irc.client.ServerConnectionError as x:
            exit(1)
        self.bot.start()



class FrontIRCBot:
    """
    """

    _message_queues = {}
    # server:port → target → Queue

    def __init__(self, nickname = DEFAULT.NICKNAME):
        self.nickname = nickname

    def privmsg(self, server, target, message):
        """
        Sends the given *message* to the given *target* on the given *server*.
        """
        server = utils.parse_server(server)

        if not server in self._message_queues:
            self._message_queues[server] = {}
            _SingleServer_FrontIRCBot_Thread(server, self.nickname,
                                             self._message_queues[server]).start()
        
        if not target in self._message_queues[server]:
            self._message_queues[server][target] = queue.Queue()

        for line in message.split('\n'):
            self._message_queues[server][target].put(line)


