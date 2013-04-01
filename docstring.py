#!/usr/bin/python
#
# Copyright (C) 2013
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# $ pytlink docstring.py
# <snip>
# Global evaluation
# -----------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10)

""" Module example for docstring and pylint """

def message(msg_user):
    ''' message to users
    Arguments
    msgUser -- Message that will be printed to users
    '''
    print "My message to users is: %s" % msg_user

if __name__ == "__main__":
    message("Looking forward to see you!")
