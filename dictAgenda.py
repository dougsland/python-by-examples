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

MAX_USERS = 2
agenda = {}

print "Agenda:"
print "================="
for user in range(MAX_USERS):
    name = raw_input('User: ')
    phone = raw_input('Phone: ')
    agenda.update({name:phone})


print "Printing data"
for name, phone in agenda.iteritems() :
    print name, phone
