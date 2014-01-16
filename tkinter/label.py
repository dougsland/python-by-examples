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

main_win = tk.Tk()

lb = tk.Label(main_win, text="hey you!")
lb.pack()

main_win.mainloop()
