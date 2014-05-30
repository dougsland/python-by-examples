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

import ConfigParser

_CONF_FILE = 'test.conf'

try:
    config = ConfigParser.RawConfigParser()
    config.read(_CONF_FILE)
    config.set('section1', 'foo', 'update_foo_data')
except ConfigParser.Error, e:
    raise e

with open(_CONF_FILE, 'w+') as configfile:
    config.write(configfile)
