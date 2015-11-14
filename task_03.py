#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Logs data from files"""
    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """creates the log"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """runs the file"""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            error = ('Can\'t open logfile {}').format(self.logfilename)
            self.log(error)
            raise IOError('Can\'t open requested file.')

        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError:
            error = ('Can\'t open logfile {}').format(self.logfilename)
            self.log(error)
        finally:
            fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
