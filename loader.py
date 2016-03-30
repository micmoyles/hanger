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
hanger.h1('Loader')
hanger.p('Under construction')
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
print ' <select name="Side" title="Side">'
print '<option value="Buy" selected>B'
print '<option value="Sell" >S'
print '<option value="Short Sell" >SS'
print '</select>'
print ' <br>'
print ' <input type="radio" name="sql" value="Show">Show Query<br>'
print ' <br>'
print '<input type="submit" value="Submit">'
print '</form>'
query = 'select * from trades'
if symbol: query+ ' where symbol = "' + str(symbol) + '"' 
if price: query+=' and price = ' + price  
if side: query+=' and side = "' + str(side) + '"'  
if counterparty: query+=' and cparty = "' + str(counterparty) + '"'  
if sql: hanger.showquery(query)
db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
cursor.close()


hanger.table(rows,cols)
hanger.h_close()
