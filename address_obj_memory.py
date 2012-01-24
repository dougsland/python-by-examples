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

myvar  = "car"
number = 15

print id(myvar)
print id(number)

# http://docs.python.org/library/functions.html
# id(object)
# Return the “identity” of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this 
# object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
#
# CPython implementation detail: This is the address of the object in memory.
