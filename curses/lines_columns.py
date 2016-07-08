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

import curses

stdscr = curses.initscr()
stdscr.addstr("Lines: %s\n" % str(curses.LINES))
stdscr.addstr("Colums: %s\n" % str(curses.COLS))
stdscr.refresh()
stdscr.getch()
curses.endwin()
