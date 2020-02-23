#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root',
                     passwd='holberton', db='super_event_storage')
