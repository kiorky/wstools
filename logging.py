#! /usr/bin/env python
"""Logging"""
import sys


class ILogger:
    '''Logger interface, by default this class
    will be used and logging calls are no-ops.
    '''
    level = 0
    def __init__(self, msg):
        return
    def warning(self, *args):
        return
    def debug(self, *args):
        return
    def error(self, *args):
        return
_LoggerClass = ILogger


class BasicLogger(ILogger):
    def __init__(self, msg, out=sys.stdout):
        self.msg, self.out = msg, out

    def warning(self, msg, *args):
        print >>self, self.WARN, self.msg,
        print >>self, msg %args
    WARN = 'WARN'
    def debug(self, msg, *args):
        print >>self, self.DEBUG, self.msg,
        print >>self, msg %args
    DEBUG = 'DEBUG'
    def error(self, msg, *args):
        print >>self, self.ERROR, self.msg,
        print >>self, msg %args
    ERROR = 'ERROR'

    def write(self, *args):
        '''Write convenience function; writes strings.
        '''
        for s in args: self.out.write(s)


def setBasicLogger():
    '''Use Basic Logger.
    '''
    setLoggerClass(BasicLogger)

def setLoggerClass(loggingClass):
    '''Set Logging Class.
    '''
    assert issubclass(loggingClass, ILogger), 'loggingClass must subclass ILogger'
    global _LoggerClass
    _LoggerClass = loggingClass

def setLevel(level=0):
    '''Set Global Logging Level.
    '''
    ILogger.level = level

def getLogger(msg):
    '''Return instance of Logging class.
    '''
    return _LoggerClass(msg)


