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

import threading


class MyProgram:
    def __init__(self):
        global _myLock
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, i):
        _myLock.acquire()
        try:
            while self._running and i > 0:
                #Return the current Thread
                #print threading.current_thread()
                print "Hello?"
                i -= 1
        finally:
            _myLock.release()


def test():
    global _myLock

    i = 3
    _myLock.acquire()
    try:
        while i > 0:
            #Return the current Thread
            #print threading.current_thread()
            print "Hi"
            i -= 1
    finally:
        _myLock.release()

if __name__ == "__main__":
    global _myLock
    _myLock = threading.Lock()
    c = MyProgram()

    t = threading.Thread(target=c.run, args=(3,))
    t.start()
    #The thread identifier
    #print t.ident

    # Wait until the thread terminates
    #t.join()

    t2 = threading.Thread(target=test, name="MyThread2")
    t2.start()
    #The thread identifier
    #print t2.ident

    # Wait until the thread terminates
    #t2.join()

    # Check if the thread2 is Daemon
    #print("%s: Is Daemon? %s" % (t2, t2.isDaemon()))

    # Setting Daemon
    #t3 = threading.Thread(target=test)
    #t3.daemon = True
    #t3.start()
    #print("%s: Is Daemon? %s" % (t3, t3.isDaemon()))
