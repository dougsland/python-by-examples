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
import shlex
import subprocess
import sys

def execute_cmd(cmd, env_shell=False):
    cmd = subprocess.Popen(shlex.split(cmd),
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=env_shell)

    output, err = cmd.communicate()
    if cmd.returncode != 0:
        print ("Cannot execute cmd [%s]" % cmd)
        return cmd.returncode

    return 0

if __name__ == "__main__":
    sys.exit(execute_cmd("touch /tmp/test"))
