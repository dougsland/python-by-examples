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

class OrdinaryPeople:
    def walk(self):
        return "Walk"

    def run(self):
        return "Run"

class Batman(OrdinaryPeople):
    def attack_running(self):
        # super() reference to OrdinaryPeople - parent class
        print("Executing %s + Punch!" % super().run())

if __name__ == "__main__":
    print("Executing batman attack!")
    superHero = Batman()
    superHero.attack_running()
