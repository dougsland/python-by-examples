#!/usr/bin/python
#
# Copyright (C) 2013
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from time import localtime

# localtime() returns a tuple
now = localtime()

year = now[0]
month = now[1]
day = now[2]

hour = now[3]
min = now[4]
sec = now[5]

wday = now[6]
yday = now[7]
isdst = now[8]

print "Year [%s] Month [%s] Day [%s] " % (year, month, day)
print "Hour [%s] Min [%s] Sec [%s] " % (hour, min, sec)

dst = lambda x: True if isdst else False
print "Weekday [%s] Day of year [%s] Is Daylight Saving Time [%s]" % (wday, yday, dst(isdst))
