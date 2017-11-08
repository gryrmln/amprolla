# See LICENSE file for copyright and license details.

"""
Logging functions
"""

from time import time
from os import makedirs
from os.path import join
import sys

from lib.config import logdir


def die(msg, tofile=True):
    """
    Log error and exit with exitcode 1
    """
    msg = "%d [ERR] %s" % (int(time()), msg)
    print(msg)
    if tofile:
        logtofile('amprolla.txt', msg+'\n')
    sys.exit(1)


def warn(msg, tofile=True):
    """
    Log warning and continue
    """
    msg = "%d [WARN] %s" % (int(time()), msg)
    print(msg)
    if tofile:
        logtofile('amprolla.txt', msg+'\n')


def info(msg, tofile=True):
    """
    Log informational message and continue
    """
    msg = "%d [INFO] %s" % (int(time()), msg)
    print(msg)
    if tofile:
        logtofile('amprolla.txt', msg+'\n')


def logtofile(filename, text, redo=False):
    """
    Log given text to a given file.
    If redo is True, rewrites the file
    """
    makedirs(logdir, exist_ok=True)
    wrt = 'a'
    if redo:
        wrt = 'w'
    lfile = open(join(logdir, filename), wrt)
    lfile.write(text)
    lfile.close()
