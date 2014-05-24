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
import os
import sys
import threading
import zipfile

from argparse import ArgumentParser


def unzip(zipname, password=None):

    zp = zipfile.ZipFile(zipname, mode="r")
    if password is not None:
        zp.setpassword(password)

    try:
        zp.extractall()
    except RuntimeError as e:
        if 'Bad password' in str(e):
            return
        else:
            raise
            
    print("Found password: %s" % password)
    zp.close()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--zipname',
                        help="name of zip",
                        required=True, nargs=1
                        )

    parser.add_argument('--passfile',
                        help="password of zip",
                        required=True, nargs=1
                        )
    args = parser.parse_args()

    if not os.path.exists(args.passfile[0]):
        sys.exit("Cannot open passfile!")

    with open(args.passfile[0], "r") as f:
        for line in f:
            t = threading.Thread(target=unzip, args=(args.zipname[0],line.strip()))
            t.start()
