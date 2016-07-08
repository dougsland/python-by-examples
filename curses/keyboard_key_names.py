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

NO_KEY_PRESSED = -1

stdscr = curses.initscr()
stdscr.nodelay(True)
curses.noecho()

# Enable the keypad ncurses return (instead of 16 bit value)
stdscr.keypad(True)

stdscr.addstr("Press q (key value 0x71) to quit the app!\n")
stdscr.refresh()

key_pressed = NO_KEY_PRESSED
while key_pressed != ord('q'):
    key_pressed = stdscr.getch()

    if key_pressed == curses.KEY_UP:
        stdscr.addstr("going up...\n")

    if key_pressed == curses.KEY_DOWN:
        stdscr.addstr("going down...\n")

    if key_pressed == curses.KEY_RIGHT:
        stdscr.addstr("going right...\n")

    if key_pressed == curses.KEY_LEFT:
        stdscr.addstr("going left...\n")

    if key_pressed == curses.KEY_F1:
        stdscr.addstr("going F1...\n")

    if key_pressed == curses.KEY_F2:
        stdscr.addstr("going F2...\n")

curses.endwin()
