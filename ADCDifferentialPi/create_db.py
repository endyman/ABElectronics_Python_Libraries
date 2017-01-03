#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 expandtab:

"""Script to initalize an sqlite database

"""

import sys
import sqlite3

DB_NAME = 'test.db'
CREATE_TABLE_STATEMENT  = '''CREATE TABLE READING ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TIMESTAMP timestamp DEFAULT CURRENT_TIMESTAMP,
    PYR1 REAL NOT NULL,
    PYR2 REAL NOT NULL);'''

def getConnection(database):
    connection = sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES)
    return connection

def createTable(connection, statement):
    connection.execute(statement)

def main():
    connection = getConnection(DB_NAME)
    try:
        createTable(connection, CREATE_TABLE_STATEMENT)
        print 'Schema create successfuly'
    except Exception as e:
        print 'An error occured create the schema: {}'.format(e)
    connection.close()

if __name__ == '__main__':
    sys.exit(main())
