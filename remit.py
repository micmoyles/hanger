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
form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">Symbol</label>
        <input type="text" name="symbol" class="form-control" id="exampleInputName2" placeholder="ECM5/ESM5">
        </td>
        <td>
        <label for="exampleInputName2">Trade Side</label>
        <input type="text" name="side" class="form-control" id="exampleInputName2" placeholder="B/S/T">
        </td>
        <td>
        <label for="exampleInputName2">Price</label>
        <input type="text" name="price" class="form-control" id="exampleInputName2" placeholder="123.45">
        </td>
        <td>
        <label for="exampleInputName2">Size</label>
        <input type="text" name="size" class="form-control" id="exampleInputName2" placeholder="100">
        </td>
        <tr>
        <td>
        <label for="exampleInputName2">Counterparty</label>
        <input type="text" name="counterparty" class="form-control" id="exampleInputName2" placeholder="Brennan">
        </td>
        <td>
        <label for="exampleInputName2">Trade ID</label>
        <input type="text" name="tradeid" class="form-control" id="exampleInputName2" placeholder="ABC123">
        </td>
        <td>
        <label for="exampleInputName2">Venue</label>
        <input type="text" name="venue" class="form-control" id="exampleInputName2" placeholder="APX/CME">
        </td>
        </tr>
    </tbody>
</table>
<button type="submit" class="btn btn-default">Submit</button>
<button type="button" class="btn btn-info">Show Query</button>
</div>
</form>
'''
#print form
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
