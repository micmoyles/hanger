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

hanger.start('Trades')
hanger.h1('Trades')
form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">Instrument</label>
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
        <label for="exampleInputName2">Quantity</label>
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
        <label for="exampleInputName2">Market</label>
        <input type="text" name="venue" class="form-control" id="exampleInputName2" placeholder="APX/CME">
        </td>
        <td>
        <label for="exampleInputName2">Segment</label>
        <input type="text" name="segment" class="form-control" id="exampleInputName2" placeholder="Something">
        </td>
        </tr>
    </tbody>
</table>
<button type="submit" class="btn btn-default">Submit</button>
<button type="button" class="btn btn-info btn-sql">Show Query</button>
<button type="button" class="btn btn-info btn-load"> Load Trades</button>
</div>
</form>
'''
print form
query = 'select TradeID,Instrument,InstrumentBegin as start,InstrumentEnd as end,Segment,Market,Side,Quantity,Price,PriceUnit,Trader,CounterParty,TradeDate from trades.trades'
def extendQuery(query,text):
  if 'where' in query:
    query+=' and '+text
  else:
    query+=' where '+text
  return query

if symbol: 
  query = extendQuery(query,"Instrument = '%s' " % str(symbol) )
if price: 
  query = extendQuery(query,"Price = %d " % float(price) )
if size: 
  query = extendQuery(query,"Quantity = %d " % float(size) )
if str(side): 
  query = extendQuery(query,"Side = '%s' " % str(side) )
if counterparty: 
  query = extendQuery(query,"CounterParty = '%s' " % str(counterparty) )
hanger.showquery(query)
if sql: 
  hanger.showquery(query)

db = mdb.connect( hanger.host, hanger.user, hanger.password )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
d = []
for row in rows:
  d.append((row['TradeID'],row['Instrument'],row['start'],row['end'],row['Segment'],row['Market'],row['Side']
            ,row['Quantity'],row['Price'],row['PriceUnit'],row['Trader'],row['CounterParty'],row['TradeDate']
))
rows = d
cursor.close()


hanger.bootstrap_table(rows,cols)
hanger.close()
