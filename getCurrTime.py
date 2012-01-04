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

import datetime

currTime = datetime.datetime.now()
####################### Year - Month - day - Hour - Minute
print currTime.strftime("Date: %Y/%m/%d Hour: %H:%M")
print currTime.strftime("myfile-%Y-%m-%d-%H:%M") + ".txt"


