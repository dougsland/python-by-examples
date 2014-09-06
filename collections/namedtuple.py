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

import collections

Dog = collections.namedtuple("Dog", "size color age")
dog = Dog("medium", "dark", 10)

print("Dog: %s, size %s, age %s" % (dog.color, dog.size, dog.age))
