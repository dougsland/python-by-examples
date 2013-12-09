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

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-f', '--foo', help="foo argument", required=True)
parser.add_argument('-b', '--bar', help="bar argument", required=True)
args = parser.parse_args()

if args.foo:
    print args.foo

if args.bar:
    print args.bar
