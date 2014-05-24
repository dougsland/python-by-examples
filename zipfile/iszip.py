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

import sys
import zipfile
    
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage: %s my_zip_file.zip"   % sys.argv[0]
        sys.exit(0)

    if zipfile.is_zipfile(sys.argv[1]):
        print("The file %s is zip file!" % sys.argv[1])
    else:
        print("%s is not a zipfile" % sys.argv[1])
