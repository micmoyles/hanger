#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys, os
import hanger as h
import MySQLdb as mdb
#form = cgi.FieldStorage()
form = cgi.SvFormContentDict()
#data = form.getfirst('mydata')
session  = form.get('session', '')
symbol	  = form.get('symbol', '')
side 	  = form.get('side', '')
sql 	  = form.get('sql', '')

host = 'localhost'
user = 'root'
passwd = 'wiarreft'
session = '20150602A'


h.bootstrap_start('Positions')
#sessions = os.system('mysql -uroot -pwiarreft -e "show databases;" | grep 201')
sessions = ['20150602A','20150603A']
h.br()
print ' <form method = "get">'
print ' Trade Date:'
print ' <select name="session" title="session">'
for s in sessions:
    print '<option value="'+str(s)+'">'+str(s)
#print '<option value="Last">'
print '</select>'
print '<input type="submit" value="Submit">'
print '</form>'
h.h1('Positions')
print ' <form method = "get">'
print ' Symbol(required):<br>'
print ' <input type="text" name="symbol">'
print ' <br>'
print ' Exchange:<br>'
print ' <input type="text" name="Exchange">'
print ' <br>'
print ' Street/House:<br>'
print ' <select name="S-H" title="S-H">'
print '<option value="House" selected>House'
print '<option value="Street" >Street'
print '</select>'
print ' <br>'
print ' <input type="radio" name="sql" value="Show">Show Query<br>'
print ' <br>'
print '<input type="submit" value="Submit">'
print ' <br>'
print '</form>'

query = 'select symbol, sum(size) as position, cparty as CounterParty from trades where'
if symbol: query = query + ' symbol = "' + str(symbol) + '" and ' 
sell_query = query + ' side = "S" group by symbol;' 
buy_query = query + ' side = "B" group by symbol;' 
if sql: h.showquery(buy_query)
db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(buy_query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
cursor.close()
h.h2('Buy Table')
h.table(rows,cols)
if sql: h.showquery(sell_query)
db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(sell_query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
cursor.close()
h.h2('Sell Table')
h.table(rows,cols)

    
h.bootstrap_close()
