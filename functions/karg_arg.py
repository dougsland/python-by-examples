#!/usr/bin/python
#
# Copyright (C) 2011-2015
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


def myfunc(*args, **kargs):
    """
    args will be tuple
    kargs will be dict
    """
    print(args)
    print(type(args))
    print(kargs)
    print(type(kargs))

if __name__ == "__main__":
    myfunc('python', 3.0, python='3.0')
