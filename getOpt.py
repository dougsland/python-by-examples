#!/usr/bin/python
#
# Copyright (C) 2012
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
import getopt

VERSION = "1.0"

def usage():
	print "Usage: " +  sys.argv[0] + " [OPTIONS]"
	print "\t--car		 \tCar name" 
	print "\t--model	 \tModel name"
	print "\t--year		 \tYear of car"
	print "\t--version       \tList version release" 
	print "\t--help          \tThis help menu\n"

	print "Example:"
	print "\t" + sys.argv[0] + " --car palio --model basic --year 2012"
	sys.exit(1)

if __name__ == "__main__":

	car   = None
	model = None
	year  = None

	try:
		opts, args = getopt.getopt(sys.argv[1:], "c:m:y:hv", ["car=", "model=", "year=", "help", "version"])
	except getopt.GetoptError, err:
		# print help information and exit:
		print(err) # will print something like "option -a not recognized"
		sys.exit(-1)

	for o, a in opts:
		if o in ("-c", "--car"):
			car = a
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-m", "--model"):
			model = a
		elif o in ("-y", "--year"):
			year = a
		elif o in ("-V", "--version"):
			print VERSION
			sys.exit(0)
		else:
			assert False, "unhandled option"
			sys.exit(-1)

	argc = len(sys.argv)
	if argc != 7:
		usage()

	print "car [%s] model [%s] year [%s]" % (car, model, year)
