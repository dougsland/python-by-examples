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

from subprocess import Popen, PIPE


def execute(cmd):
    ret = []
    try:
        p = Popen(cmd, stdout=PIPE)
        ret = [p.communicate()[0], p.returncode]
    except OSError, e:
        print "Cannot execute command: %s" % e

    return ret

myCmd = ["ls", "-la"]
ret = execute(myCmd)

if ret:
    print "return output:\n%s" % ret[0]
    print "return code:\n%s" % ret[1]
