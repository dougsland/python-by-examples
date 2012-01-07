#!/usr/bin/python
#
# Copyright (C) 2011
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

try:
	fd = open('/tmp/test', 'w')
	fd.write("test")
except IOError:
	print "error"

finally:	
	fd.close()
