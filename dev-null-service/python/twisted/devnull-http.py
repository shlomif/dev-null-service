#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the MIT license.

"""
devnull HTTP
"""
from twisted.internet import endpoints, protocol, reactor


class Echo(protocol.Protocol):
    BEFORE_HEADER = 0
    AFTER_HEADER = 1
    HEADER_ERROR = 2
    MAX_HEADER_LEN = 1024

    def __init__(self):
        super(Echo, self).__init__()
        self.state = self.BEFORE_HEADER
        self.header = bytes()

    def dataReceived(self, data):  # noqa: N802
        if self.state == self.BEFORE_HEADER:
            self.header += data
            if "\r\n\r\n".encode('utf-8') in self.header:
                self.state = self.AFTER_HEADER
                self.transport.write(
                    ("HTTP/1.1 200 OK\r\nContent-Type: text/html" +
                     "\r\n\r\n<html></html>").encode('utf-8'))
                self.transport.loseConnection()
            elif len(self.header) > self.MAX_HEADER_LEN:
                self.state = self.HEADER_ERROR


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):  # noqa: N802
        return Echo()


endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()
