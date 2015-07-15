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

import sys

if sys.platform == 'win32':
    print("Platform is Win32 based!")
else:
    print('{0}'.format(sys.platform))
