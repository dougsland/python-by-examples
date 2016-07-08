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

def center_msg(row, screen, message):
    rows, cols = screen.getmaxyx()
    position = cols - len(message)
    position /= 2
    screen.addstr(row, position, message)
    stdscr.refresh()

stdscr = curses.initscr()
center_msg(5, stdscr, "super_test")
stdscr.getch()
curses.endwin()

