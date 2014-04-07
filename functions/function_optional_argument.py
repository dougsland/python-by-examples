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

def carInfo(name, model=None):

    if model == None:
        print "Car name: %s" % name
    else:
        print "Car name: %s model %s" % (name, model)


if __name__ == "__main__":
    carInfo("Fiesta")
    carInfo("Doblo", "2012")
