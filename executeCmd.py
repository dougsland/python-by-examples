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

import subprocess

def runCmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, error) = process.communicate()

    # output
    # print output

    # Let's return the exit value
    return process.poll()

if __name__ == "__main__":
    cmd = "ls -la ."
    print runCmd(cmd)
