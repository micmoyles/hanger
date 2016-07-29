#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
form = cgi.SvFormContentDict()
AssetType	  = form.get('AssetType', '')
AssetID 	  = form.get('AssetID', '')
FuelType          = form.get('FuelType', '')
AssetDescription  = form.get('AssetDescription','')
name              = form.get('name', '')
sql 	  = form.get('sql', '')

session = 'config'
db = mdb.connect( hanger.host, hanger.user, hanger.password )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
hanger.start('Plant Config')
hanger.h1('Plant Config')
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
        </tr>
    </tbody>
</table>
<button type="Query" class="btn btn-default">Query</button>
<button type="Add" class="btn btn-default">Add</button>
<button type="button" class="btn btn-info">Show Query</button>
</div>
</form>
'''
print form
query = 'select *  from plants'
def extendQuery(query,text):
  if 'where' in query:
    query+=' and '+text
  else:
    query+=' where '+text
  return query

if EventStatus: 
  query = extendQuery(query,"EventStatus = %d " % str(EventStatus) )
if AffectedUnit: 
  query = extendQuery(query,"AffectedUnit = %f " % str(AffectedUnit) )
if EventType: 
  query = extendQuery(query,"EventType = '%s' " % str(EventType) )
if AssetID: 
  query = extendQuery(query,"AssetID = '%s' " % str(AssetID))
if MessageHeading: 
  query = extendQuery(query,"MessageHeading = %s " % str(MessageHeading))
hanger.showquery(query)
if sql: 
  hanger.showquery(query)

cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
#cols = ['AffectedUnitEIC','AssetType','AffectedUnit','DurationUncertainty','RelatedInformation','AssetId','EventType','NormalCapacity','AvailableCapacity','EventStatus','EventStart','EventEnd','Cause','FuelType','Participant_MarketParticipantID','MassageHeading']
cols = ['Name, AssetID, FuelType, NormalCapacity','CurrentCapacity']
rows = cursor.fetchall()
cursor.close()
d = []
for row in rows:
  d.append((str(row['name']), 
           str(row['AssetId']),
           row['NormalCapacity'],
           row['AvailableCapacity'],
           str(row['FuelType']),
))
rows = d


hanger.bootstrap_table(rows,cols)
hanger.close()
