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
session = '20150602A'
hanger.bootstrap_start('Trades')
hanger.h1('Trades')
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
print form
query = 'select * from trades'
def extendQuery(query,text):
  if 'where' in query:
    query+=' and '+text
  else:
    query+=' where '+text
  return query

if symbol: 
  query = extendQuery(query,"symbol = '%s' " % str(symbol) )
if price: 
  query = extendQuery(query,"price = %d " % float(price) )
if str(side): 
  query = extendQuery(query,"side = '%s' " % str(side) )
if counterparty: 
  query = extendQuery(query,"cparty = '%s' " % str(counterparty) )
hanger.showquery(query)
if sql: 
  hanger.showquery(query)

db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
cursor.close()


hanger.bootstrap_table(rows,cols)
#hanger.h_close()
hanger.bootstrap_close()
