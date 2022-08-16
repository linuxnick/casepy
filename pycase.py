#!/usr/bin/env python

from __future__ import print_function
import sys

def start():
    print("Starting application...")

def stop():
    print("Stopping application...")

def restart():
    stop()
    start()

def help(argv):
    print("{0} [start|stop|restart]".format(argv[0]))
    sys.exit(1)

switcher = {
    "start": start,
    "stop": stop,
    "restart": restart
}

try:
    arg = sys.argv[1]
    switcher.get(arg, lambda: help(sys.argv))()
except IndexError:
    help(sys.argv)
