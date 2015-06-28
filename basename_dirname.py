#!/usr/bin/python
#
# Copyright (C) 2015
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
import os

path = "/etc/pki/cert/ca.pem"

print("The file {0} is located in the dir {1}".format(
    os.path.basename(path),
    os.path.dirname(path)
))
