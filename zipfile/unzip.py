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
import zipfile

from argparse import ArgumentParser


def unzip(zipname, password=None):

    zp = zipfile.ZipFile(zipname, mode="r")
    if password is not None:
        zp.setpassword(password[0])

    try:
        for f in zp.namelist():
            print("Extracting %s" % f)
            zp.extract(f)
    except RuntimeError as e:
        if 'encrypted' in str(e):
            sys.exit("zipfile requires password!")
        if 'Bad password' in str(e):
            sys.exit("Bad password to uncompress the files!")
        else:
            raise
    # Extract all members from the archive
    # zp.extractall()
    zp.close()
    print("Done, created %s" % zipname)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--zipname',
                        help="name of zip",
                        required=True, nargs=1
                        )

    parser.add_argument('--password',
                        help="password of zip",
                        required=False, nargs=1
                        )
    args = parser.parse_args()

    unzip(
        zipname=args.zipname[0],
        password=args.password
    )
