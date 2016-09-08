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

form = '''
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
<button type="button" class="btn btn-info btn-sql">Show Query</button>
<button type="button" class="btn btn-updateBook">Update Book</button>
</div>
</form>

'''

h.start('Positions')
h.br()
print form

query = '''select irl.timestamp as segment, irl.position as irl, uk.position as uk, nl.position as nl from irl  
	join nl on nl.timestamp = irl.timestamp 
	join uk on uk.timestamp = irl.timestamp
'''
h.showquery(query)
db = mdb.connect( h.host, h.user, h.password )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use position" )
cursor.execute(query)
cols = ['Segment','IRL','UK','NL'] 
rows = cursor.fetchall()
d = []
for row in rows:
  d.append((str(row['segment']),row['irl'],row['uk'],row['nl']))
rows = d
cursor.close()
h.h2('HH Positions')
h.bootstrap_table(rows,cols)

    
h.close()
