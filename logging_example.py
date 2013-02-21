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

import logging

logging.basicConfig(format='%(asctime)s %(name)s %(message)s', filename='my.log', level=logging.DEBUG)
logger = logging.getLogger("appname")
# Do not append use 'filemode'
# logging.basicConfig(filename='my.log', filemode='w', level=logging.DEBUG)

def calc(value):
    logger.info('original variable value [%s]', value)
    new_value = value * 10
    logger.info('new value [%s]', new_value)
    return new_value

def main():
    logger.info("starting my simple program..")
    calc(2)

if __name__ == '__main__':
    main()
