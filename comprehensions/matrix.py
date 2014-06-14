#!/usr/bin/python
#
# Copyright (C) 2011-2014
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

numbers = [
    [5, 6, 7],
    [7, 6, 5],
    [5, 6, 9]
]

# Get the position 2 from each nested list
final_list = [number[2] for number in numbers]
print("final list: %s" % final_list)
