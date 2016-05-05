#!/usr/bin/python
#
# Copyright (C) 2016
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

from rpmUtils.miscutils import compareVerOnly
from itertools import combinations


def check_higher_kernel(path=None):
    """
    Check through kernel modules dir, the higher version
    available

    path -- The path to kernel modules dir
    """
    higher_kernel = None

    if path is None:
        modules_dir = "/lib/modules"
    else:
        modules_dir = "{0}/lib/modules".format(path)

    modules_dir = os.listdir(modules_dir)
    for km1, km2 in combinations(modules_dir, 2):
        ret = compareVerOnly(km1, km2)
        # Extra validation via rpmUtils.miscutils to
        # check if new value in km1 or in km2 is higher than
        # the current hold in higher_kernel
        if ret == 1:
            if higher_kernel is None or \
                    compareVerOnly(km1, higher_kernel) == 1:
                higher_kernel = km1
        elif ret == -1:
            if higher_kernel is None or \
                    compareVerOnly(km2, higher_kernel) == 1:
                higher_kernel = km2

    return higher_kernel

print(check_higher_kernel())
