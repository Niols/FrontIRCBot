FrontIRCBot [![Build Status][travis-build-status]][travis-repo]
===========

FrontIRCBot is a little interface between the [irc][pypi-irc] lib and you.
It handles multiple irc servers at the same time. It also works in threads, which means you can really use it as a front for any python application, without having to think about how you will have your application working with irc.


Requirements
------------

FrontIRCBot requires [irc][pypi-irc].

FrontIRCBot requires `python >= 2.7` or `python >= 3.2`.
`python2.6` is not supported because of FrontIRCBot's dependency in [irc][pypi-irc].





[travis-repo]: https://travis-ci.org/Niols/FrontIRCBot
[travis-build-status]: https://travis-ci.org/Niols/FrontIRCBot.svg?branch=master

[pypi-irc]: https://pypi.python.org/pypi/irc/12.1.4
