#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
form = cgi.SvFormContentDict()
eventstatus= form.get('eventstatus', '')
timewindow = form.get('timewindow', '')
fueltype = form.get('fueltype', '')
outputratio	  = form.get('outputratio', '')
emailaddress = form.get('emailaddress', '')
tradeid   = form.get('tradeid', '')
venue     = form.get('venue', '')
counterparty	  = form.get('counterparty', '')
sql 	  = form.get('sql', '')

hanger.start('Alert Configuration')
phone_alert_form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">Michael Brennan</label>
        <select class='form-control'>
          <option>Available</option>
          <option>Not Available</option>
          <option>Bad Mood</option>
        </td>
        <td>
        <label for="exampleInputName2">Number</label>
        <select class='form-control'>
          <option>0860802648</option>
        </td>
	<td>
	<button type="submit" class="btn btn-success">Available</button>
	</td>
	</tr>
        <tr>
        <td>
        <label for="exampleInputName2">Matt Golden</label>
        <select class='form-control'>
          <option>Available</option>
          <option>Not Available</option>
        </td>
        <td>
        <label for="exampleInputName2">Number</label>
        <select class='form-control'>
          <option>0861234567</option>
        </td>
	<td>
	<button type="submit" class="btn btn-danger">Unavailable</button>
	</td>
	</tr>
    </tbody>
</table>
<button type="submit" class="btn btn-default">Update</button>
</div>
</form>
'''
email_alert_form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleinputname2">event status</label>
        <select class='form-control'>
          <option>open</option>
          <option>future</option>
        </td>
	</tr>
	<tr>
        <td>
        <label for="exampleinputname2">fuel type</label>
        <select class='form-control'>
          <option>coal</option>
          <option>nuclear</option>
          <option>ccgt</option>
          <option>other</option>
        </td>
	</tr>
	<tr>
        <td>
        <label for="exampleinputname2">output ratio</label>
        <input type="text" name="outputratio" class="form-control" id="exampleinputname2" placeholder="25%">
        </td>
	</tr>
	<tr>
        <td>
        <label for="exampleinputname2">time window</label>
        <input type="text" name="timewindow" class="form-control" id="exampleinputname2" placeholder="hours">
        </td>
        </tr>
	<tr>
        <td>
        <label for="exampleinputname2">email address</label>
        <input type="text" name="emailaddress" class="form-control" id="exampleinputname2" placeholder="alert@erova">
        </td>
        </tr>
    </tbody>
</table>
<button type="submit" class="btn btn-default">submit</button>
<button type="button" class="btn btn-info btn-sql">show query</button>
</div>
</form>
'''
print '<div class="container col-md-6">'
hanger.h1('email alerts')
print email_alert_form
if eventstatus and fueltype and outputratio and timewindow and emailaddress:
  print '''<div class='container'>
 <button type="button" class="btn btn-success btn-lg"> Success - new alert added </button>
 <button type="button" class="btn btn-success btn-lg"> %s %s %s %s %s  </button>
</div>
''' % (side, symbol, venue, size, price )
else:
  print '''<div class='container'>
 <button type="button" class="btn btn-warning"> All parameters required to add new alert </button>
</div>
''' 
print '</div>'
print '<div class="container col-md-6">'
hanger.h1('Phone Contacts')
print phone_alert_form
print '</div>'
hanger.close()
