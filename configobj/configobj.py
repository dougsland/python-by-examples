#!/usr/bin/python
#
# Copyright (C) 2016
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from configobj import ConfigObj


def hasconf(filename, key, value):
    """
    Validates a value against a key from a config file

    Returns:
    True if value matches (case insensitive)
    False if value doesn't match
    raise if no key found
    """
    cfg = ConfigObj(filename)

    try:
        if cfg[key].lower() == value.lower():
            return True

        return False

    except KeyError:
        raise

print(hasconf('/etc/os-release', 'NAME', 'Fedora'))
