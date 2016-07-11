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

if curses.has_colors():
    curses.start_color()
    stdscr.addstr("Color pairs [%s]" % curses.color_pair(1))
    stdscr.addstr("Colors [%s]" % curses.COLORS)

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    stdscr.bkgd(' ', curses.color_pair(2))

    # or a background char '.'
    # stdscr.bkgd('.', curses.color_pair(2))

stdscr.move(2,10)
stdscr.addstr("string")
stdscr.addstr("Pretty text", curses.color_pair(1))
stdscr.getch()
curses.endwin()
