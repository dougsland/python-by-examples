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

# Enable the keypad ncurses return (instead of 16 bit value)
stdscr.keypad(True)

# Refresh after attributes
stdscr.refresh()

# No echo to screen
curses.noecho()

# Remove cursor
curses.curs_set(0)

win1 = curses.newwin(0,0,0,0)
win1.box()
win1.addstr(1,1,"Press q to quit or F1 for help menu, use arrow keys!")

key_pressed = NO_KEY_PRESSED
while key_pressed != ord('q'):
    key_pressed = stdscr.getch()

    if key_pressed == curses.KEY_UP:
        win1.addstr(2,1,"going up...")

    if key_pressed == curses.KEY_DOWN:
        stdscr.addstr(2,1,"going down...")

    if key_pressed == curses.KEY_RIGHT:
        stdscr.addstr(2,1,"going right...")

    if key_pressed == curses.KEY_LEFT:
        stdscr.addstr(2,1,"going left...")

    if key_pressed == curses.KEY_F1:

        win2 = curses.newwin(20,50,10,20)
        win2.box()
        win2.addstr(1,1,"F1 key pressed, enter to return!")
        win2.refresh()
        win2.getch()
        del win2

        # Make ncurses believe all chars from win1 get updated, next
        # refresh will re-draw
        win1.touchwin()

    if key_pressed == curses.KEY_F2:
        stdscr.addstr(2,1,"going F2...\n")

    stdscr.refresh()
    win1.refresh()

curses.endwin()
