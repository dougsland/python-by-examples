#!/usr/bin/python
#
# Copyright (C) 2011-2014
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


class Person:
    id_person = 0

    def __init__(self, name):
        self.id_person = Person.id_person
        Person.id_person += 1
        self.name = name
        print("Person name %s id:%d" %
              (self.name, self.id_person))


if __name__ == "__main__":
    p = Person("Scooby")
    p2 = Person("Junior")
    p3 = Person("Clara")
