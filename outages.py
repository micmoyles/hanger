#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
#form = cgi.FieldStorage()
form = cgi.SvFormContentDict()
EventStatus	  = form.get('EventStatus', '')
AssetType	  = form.get('AssetType', '')
AffectedUnit 	  = form.get('AffectedUnit', '')
AssetID 	  = form.get('AssetID', '')
EventType         = form.get('EventType', '')
FuelType          = form.get('FuelType', '')
sql 	  = form.get('sql', '')

session = 'REMIT'
hanger.start('Outages')
hanger.h1('Outages')
form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">Event Status</label>
        <input type="text" name="EventStatus" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Asset Type</label>
        <input type="text" name="AssetType" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Affected Unit</label>
        <input type="text" name="AffectedUnit" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Asset ID</label>
        <input type="text" name="AssetID" class="form-control" id="exampleInputName2">
        </td>
        <tr>
        <td>
        <label for="exampleInputName2">Event Type</label>
        <input type="text" name="EventType" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Fuel Type</label>
        <input type="text" name="FuelType" class="form-control" id="exampleInputName2">
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
query = 'select *  from outages'
def extendQuery(query,text):
  if 'where' in query:
    query+=' and '+text
  else:
    query+=' where '+text
  return query

if size: 
  query = extendQuery(query,"TQ = %d " % int(size) )
if price: 
  query = extendQuery(query,"PT = %f " % float(price) )
if interconnectorID: 
  query = extendQuery(query,"IC = '%s' " % str(interconnectorID) )
if TD: 
  query = extendQuery(query,"TD = '%s' " % str(TD) )
if TT: 
  query = extendQuery(query,"TT = %d " % int(TT) )
if settlement: 
  query = extendQuery(query,"ST = %d " % str(settlement) )
hanger.showquery(query)
if sql: 
  hanger.showquery(query)

db = mdb.connect( hanger.host, hanger.user, hanger.password )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
#cols = ['AffectedUnitEIC','AssetType','AffectedUnit','DurationUncertainty','RelatedInformation','AssetId','EventType','NormalCapacity','AvailableCapacity','EventStatus','EventStart','EventEnd','Cause','FuelType','Participant_MarketParticipantID','MassageHeading']
cols = ['AffectedUnit','AssetId','EventType','NormalCapacity','AvailableCapacity','EventStatus','EventStart','EventEnd','FuelType']
rows = cursor.fetchall()
cursor.close()
d = []
for row in rows:
  d.append(( str(row['AffectedUnit']),
           str(row['AssetId']),
           str(row['EventType']),
           row['NormalCap'],
           row['AvailCap'],
           str(row['EventStatus']),
           str(row['EventStart']),
           str(row['EventEnd']),
           str(row['FuelType'])
))
rows = d


hanger.bootstrap_table(rows,cols)
hanger.close()
