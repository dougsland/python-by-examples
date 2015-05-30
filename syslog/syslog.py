#!/usr/bin/python
#
# Copyright (C) 2013-2015
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
import syslog

if sys.version_info >= (2, 7, 0):
    syslog.syslog(syslog.LOG_INFO, "Sending this msg to /var/log/messages")

# Priority levels (high to low):
#    LOG_EMERG, LOG_ALERT, LOG_CRIT, LOG_ERR, LOG_WARNING,
#    LOG_NOTICE, LOG_INFO, LOG_DEBUG.
# More info: https://docs.python.org/2/library/syslog.html
