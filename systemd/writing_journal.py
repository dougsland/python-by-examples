#!/usr/bin/python
#
# Copyright (C) 2012-2015
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import logging

# Requires the package systemd-python
from systemd import journal


def _set_logger():
    """
    Set the logging schema
    """
    log = logging.getLogger(__name__)
    log.propagate = False
    log.setLevel(logging.DEBUG)
    log.addHandler(
        journal.JournalHandler(SYSLOG_IDENTIFIER='my app')
    )
    return log

if __name__ == "__main__":
    logger = _set_logger()
    logger.debug("debugging message")
    logger.info("info message")
    # To check the message, execute: journalctl -xr
