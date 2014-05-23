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

class MyTest:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test(self):
        print "My car is %s, year %s" % (self.x, self.y)

if __name__ == "__main__":
    c = MyTest("fiat", "2010")
    c.test()
