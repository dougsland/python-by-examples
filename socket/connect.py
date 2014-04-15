#!/usr/bin/python
#
# Copyright (C) 2014
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import socket
import struct
import sys

_TIMEOUT_SEC = 3

def _connect(ip, port):
    socket.setdefaulttimeout(_TIMEOUT_SEC)
    sk = socket.socket()

    # connect() requires tuple
    sk.connect((ip, port))
    print str(sk.recv(1024)).strip()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "print daemon banner"
        print "Usage: %s host port"   % sys.argv[0]
        print "Example: %s 192.168.1.60 22" % sys.argv[0]
        sys.exit(0)

    try:
        _connect(sys.argv[1], int(sys.argv[2]))
    except socket.timeout as e:
        print "timeout connecting %s:%s" % (sys.argv[1], sys.argv[2])
