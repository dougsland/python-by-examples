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

myvar = "car"

print "myvar value = [%s] %s" % (myvar, type(myvar))

myvar = True

print "myvar value = [%s] %s" % (myvar, type(myvar))

myvar = 1

print "myvar value = [%s] %s" % (myvar, type(myvar))

myvar = 1.1

print "myvar value = [%s] %s" % (myvar, type(myvar))

myvar = 51j

print "myvar value = [%s] %s" % (myvar, type(myvar))

myvar = 123456L
print "myvar value = [%s] %s" % (myvar, type(myvar))

myvar = 0x80
print "myvar value = [%s] %s" % (myvar, type(myvar))

myvar = -500
print "myvar value = [%s] %s" % (myvar, type(myvar))
