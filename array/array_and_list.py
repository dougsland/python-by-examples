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

from array import array

list_data = ['uno', 2009, 'white']
array_data = array('l', [2009, 2008, 2007, 2006])

print "Type vars on array:"
for t in array_data:
    print "data: %s type: %s" % (t, type(t))

print "Type vars on list:"
for t in list_data:
    print "data: %s type: %s" % (t, type(t))
