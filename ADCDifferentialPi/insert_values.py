#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 expandtab:

"""Script to insert readings into an sqlite database

"""

from ABE_ADCDifferentialPi import ADCDifferentialPi
from ABE_helpers import ABEHelpers
import sys
import sqlite3
import datetime

DB_NAME = 'test.db'

def getConnection(database):
    connection = sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES)
    return connection

def insertData(connection, pyr1, pyr2):
    connection.execute('INSERT INTO READING(TIMESTAMP, PYR1, PYR2) VALUES("{}", {:f}, {:f})'.format(str(datetime.datetime.now()), pyr1, pyr2))
    connection.commit()

def main():
    connection = getConnection(DB_NAME)
    try:
        i2c_helper = ABEHelpers()
        bus = i2c_helper.get_smbus()
        adc = ADCDifferentialPi(bus, 0x68, 0x69, 18)
        insertData(connection, adc.read_voltage(1), adc.read_voltage(2))
    except Exception as e:
        print 'An error occured inserting data: {}'.format(e)
    connection.close()

if __name__ == '__main__':
    sys.exit(main())
