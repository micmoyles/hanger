#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
#form = cgi.FieldStorage()
form = cgi.SvFormContentDict()
pubTsfrom	  = form.get('pubTsfrom', '')
pubTsto	  = form.get('pubTsto', '')
price 	  = form.get('price', '')
size 	  = form.get('size', '')
TD   = form.get('TD', '')
TT   = form.get('TT', '')
interconnectorID     = form.get('interconnectorID', '')
settlement	  = form.get('settlement', '')
sql 	  = form.get('sql', '')

session = 'REMIT'
hanger.start('Trade Prints')
hanger.h1('Trade Prints')
form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">pubTs from</label>
        <input type="text" name="pubTs" class="form-control" id="exampleInputName2" placeholder="20160714 14:00:00">
        </td>
        <td>
        <label for="exampleInputName2">pubTs to</label>
        <input type="text" name="pubTs" class="form-control" id="exampleInputName2" placeholder="20160714 14:00:00">
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
        <label for="exampleInputName2">InterConnectorID</label>
        <input type="text" name="interconnectorID" class="form-control" id="exampleInputName2" >
        </td>
        <td>
        <label for="exampleInputName2">TT</label>
        <input type="text" name="TT" class="form-control" id="exampleInputName2" placeholder="BALIT_RTE">
        </td>
        <td>
        <label for="exampleInputName2">TD</label>
        <input type="text" name="TD" class="form-control" id="exampleInputName2" placeholder="A01">
        </td>
        <td>
        <label for="exampleInputName2">Settlement Time</label>
        <input type="text" name="settlement" class="form-control" id="exampleInputName2" placeholder="20160715 15:00:00">
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
query = 'select * from SOSO'
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
hanger.close()
