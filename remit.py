#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
#form = cgi.FieldStorage()
form = cgi.SvFormContentDict()
symbol	  = form.get('symbol', '')
price 	  = form.get('price', '')
side 	  = form.get('side', '')
size 	  = form.get('size', '')
tradeid   = form.get('tradeid', '')
venue     = form.get('venue', '')
counterparty	  = form.get('counterparty', '')
sql 	  = form.get('sql', '')

host = 'localhost'
user = 'root'
passwd = 'wiarreft'
session = 'REMIT'
hanger.start('System Frequency')
hanger.h1('System Frequency')
query = 'select timestamp, freq as SystemFrequency  from frequency'

hanger.showquery(query)
if sql: 
  hanger.showquery(query)

db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
cols = ['Timestamp','Frequency']
rows = cursor.fetchall()
cursor.close()

d = []
for row in rows:
  d.append((str(row['timestamp']),row['SystemFrequency']))
rows = d

hanger.bootstrap_table(rows,cols)
#hanger.h_close()
hanger.close()
