#!/usr/bin/python
#
# Copyright (C) 2014
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
import zipfile
try:
    import zlib
    comp = zipfile.ZIP_DEFLATED
except:
    comp = zipfile.ZIP_STORED

from argparse import ArgumentParser


def zip(zipname, file_to_compress):

    zp = zipfile.ZipFile(zipname,
                         mode="w",
                         compression=comp
                         )

    for f in file_to_compress:
        if not os.path.exists(f):
            print("Cannot find %s, continuing.." % f)
            continue
        zp.write(f)

    zp.close()
    print("Done, created %s" % zipname)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--file',
                        help="file(s) to zip",
                        required=True, nargs='+'
                        )

    parser.add_argument('--zipname',
                        help="name of zip",
                        required=True, nargs=1
                        )
    args = parser.parse_args()

    zip(
        zipname=args.zipname[0],
        file_to_compress=args.file
    )
