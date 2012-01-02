#!/usr/bin/python
#
# Copyright (C) 2012
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage: %s my_host_name"   % sys.argv[0]
        print "Example: %s 192.168.1.60" % sys.argv[0]
        sys.exit(1)

    print "Hostname %s" % sys.argv[1]
