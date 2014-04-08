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

def build_car(**kargs):
    """ kargs is a dict """
    for k,v in kargs.items():
        print "Key: %s Value: %s" % (k, v)

if __name__ == "__main__":
    build_car(car="fiat", color="red", year="1982")
    build_car(car="fiat", color="red")
