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
stdscr.addstr("text")
stdscr.move(1,0)
stdscr.addstr("text")
stdscr.refresh()
stdscr.getch()
stdscr.move(0,0)
stdscr.clrtoeol()
stdscr.getch()
curses.endwin()
