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

import re

# Compile the regular expression. It's possible to use it often
exp = re.compile('.ambo*')

strtest = "The rambo movie is the best. Rambo needs a new movie!"
print(exp.findall(strtest))

strtest2 = "Is really rambo a good movie? Currently, rambo is too old!"
print(exp.findall(strtest2))
