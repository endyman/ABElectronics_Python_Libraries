#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 expandtab:

"""Script to read readings from an sqlite database

"""

import sys
import sqlite3
import datetime

DB_NAME = 'test.db'
CSV_DELIMITER = ';'

def getConnection(database):
    connection = sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES)
    return connection

def getData(connection):
    cursor = connection.execute('SELECT * from READING')
    print 'id;timestamp;pyr1;pyr2'
    for row in cursor:
        print '{}{}{}{}{:f}{}{:f}'.format(row[0], CSV_DELIMITER, str(row[1]), CSV_DELIMITER, row[2], CSV_DELIMITER, row[3])

def main():
    connection = getConnection(DB_NAME)
    try:
        getData(connection)
    except Exception as e:
        print 'An error occured getting data: {}'.format(e)
    connection.close()

if __name__ == '__main__':
    sys.exit(main())
