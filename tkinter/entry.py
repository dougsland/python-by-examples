#!/usr/bin/python
#
# Copyright (C) 2013
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
if sys.version_info >= (3, 0):
    import tkinter as tk
else:
    import Tkinter as tk

def callback():
    print txt.get()

main_win = tk.Tk()
main_win.title("entry test")

txt = tk.Entry(main_win, width=30)
txt.pack()
txt.focus_set()

bt = tk.Button(main_win, text="Collect", width=10, command=callback)
bt.pack()

main_win.mainloop()
