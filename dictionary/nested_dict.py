#!/usr/bin/python
#
# Copyright (C) 2011-2014
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

data = {
    'name': {'first': 'doug', 'middle': 'sch'},
    'age': 32,
    'cars': ['fiat', 'ford']
}

# When looping through dictionaries, the key and corresponding value can
# be retrieved at the same time using the iteritems() method.
for key, value in data.iteritems():
    print("%s: %s " % (key, value))
