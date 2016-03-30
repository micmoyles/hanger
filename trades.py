#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
#form = cgi.FieldStorage()
form = cgi.SvFormContentDict()
#data = form.getfirst('mydata')
symbol	  = form.get('symbol', '')
price 	  = form.get('price', '')
side 	  = form.get('side', '')
counterparty	  = form.get('counterparty', '')
sql 	  = form.get('sql', '')

host = 'localhost'
user = 'root'
passwd = 'wiarreft'
session = '20150602A'

hanger.h_start()
hanger.menu()
hanger.h1('Trades')
print ' <form method = "get">'
print ' Symbol:<br>'
print ' <input type="text" name="symbol">'
print ' <br>'
print ' Price:<br>'
print ' <input type="text" name="price">'
print ' <br>'
print ' CounterParty:<br>'
print ' <input type="text" name="counterparty">'
print ' <br>'
print ' Side:<br>'
print '<select name="side" title="side">'
print '<option value="All" selected>A'
print '<option value="Buy">B'
print '<option value="Sell" >S'
print '<option value="Short Sell" >SS'
print '</select>'
print ' <br>'
print ' <input type="radio" name="sql" value="Show">Show Query<br>'
print ' <br>'
print '<input type="submit" value="Submit">'
print '</form>'
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
if str(side) != 'All': 
  query = extendQuery(query,"side = '%s' " % str(side) )
if counterparty: 
  query = extendQuery(query,"cparty = '%s' " % str(counterparty) )
#  query+=' and cparty = "' + str(counterparty) + '"'  
if sql: 
  hanger.showquery(query)
db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
cursor.close()


hanger.table(rows,cols)
hanger.h_close()
