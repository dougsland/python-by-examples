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

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
print("numbers list: %s" % numbers_list)
print("numbers list: type %s\n" % type(numbers_list))

# Generate from the above list, the pair numbers list
pair_numbers_list = [number for number in numbers_list if number % 2 == 0]

print("pair numbers list: %s" % pair_numbers_list)
print("pair numbers list: type %s" % type(pair_numbers_list))
