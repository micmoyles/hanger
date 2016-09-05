#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
form = cgi.SvFormContentDict()
symbol	  = form.get('symbol', '')
price 	  = form.get('price', '')
side 	  = form.get('side', '')
size 	  = form.get('size', '')
tradeid   = form.get('tradeid', '')
venue     = form.get('venue', '')
counterparty	  = form.get('counterparty', '')
sql 	  = form.get('sql', '')

hanger.start('Trade Reporting')
hanger.h1('Report Trade')
form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">Traded Instrument</label>
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
        <select class='form-control'>
          <option>APX</option>
          <option>Elexon</option>
          <option>EMCF</option>
          <option>Rencap</option>
      
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
<button type="button" class="btn btn-info btn-sql">Show Query</button>
</div>
</form>
'''
print form
if symbol and venue and size and size:
  print '''<div class='container'>
 <button type="button" class="btn btn-success btn-lg"> Success - trade report sent </button>
 <button type="button" class="btn btn-success btn-lg"> %s %s %s %s %s  </button>
</div>
''' % (side, symbol, venue, size, price )
else:
  print '''<div class='container'>
 <button type="button" class="btn btn-warning"> Cannot submit trade without all required parameters </button>
</div>
''' 

hanger.close()
