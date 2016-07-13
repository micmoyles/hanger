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
venue	  = form.get('venue', '')
counterparty = form.get('counterparty', '')

host = 'localhost'
user = 'root'
passwd = 'wiarreft'
session = '20150602A'
form = '''
<form method = "get">
 Trade Date:
 <select name="session" title="session">
<option value="20150602A">20150602A
<option value="20150603A">20150603A
</select>
<input type="submit" value="Submit">
</form>
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">Symbol</label>
        <input name="symbol" type="text" class="form-control" id="exampleInputName2" placeholder="ECM5/ESM5">
        </td>
        <td>
        <label for="exampleInputName2">Trade Side</label>
        <input name="side" type="text" class="form-control" id="exampleInputName2" placeholder="B/S/T">
        </td>
        <td>
        <label for="exampleInputName2">Counterparty</label>
        <input name="counterparty" type="text" class="form-control" id="exampleInputName2" placeholder="Brennan">
        </td>
        <td>
        <label for="exampleInputName2">Venue</label>
        <input name="venue" type="text" class="form-control" id="exampleInputName2" placeholder="APX/CME">
        </td>
        </tr>
    </tbody>
</table>

<button type="submit" class="btn btn-default">Submit</button>
<button type="button" class="btn btn-info">Show Query</button>
<button type="button" class="btn btn-updateBook">Update Book</button>
</div>
</form>

'''

h.start('Positions')
#sessions = os.system('mysql -uroot -pwiarreft -e "show databases;" | grep 201')
sessions = ['20150602A','20150603A']
h.br()
print form

query = 'select symbol, sum(size) as position, cparty as CounterParty from trades where'
if symbol: query = query + ' symbol = "' + str(symbol) + '" and ' 
if counterparty: query = query + ' cparty = "' + str(counterparty) + '" and ' 
sell_query = query + ' side = "S" group by symbol;' 
buy_query = query + ' side = "B" group by symbol;' 
h.showquery(buy_query)
db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(buy_query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
cursor.close()
h.h2('Buy Table')
h.bootstrap_table(rows,cols)
h.showquery(sell_query)
db = mdb.connect( host, user, passwd )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(sell_query)
cols = map(lambda x: x[0], cursor.description) 
rows = cursor.fetchall()
cursor.close()
h.h2('Sell Table')
h.bootstrap_table(rows,cols)

    
h.bootstrap_close()
