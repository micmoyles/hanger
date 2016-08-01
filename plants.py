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
Name              = form.get('Name', '')
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
        <label for="exampleInputName2">Name</label>
        <input type="text" name="Name" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Asset Type</label>
        <input type="text" name="AssetType" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Asset Description</label>
        <input type="text" name="AssetDescription" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Asset ID</label>
        <input type="text" name="AssetID" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Fuel Type</label>
        <input type="text" name="FuelType" class="form-control" id="exampleInputName2">
        </td>
    </tbody>
</table>
<button type="Query" class="btn btn-default">Query</button>
<button type="Add" class="btn btn-default">Add</button>
<button type="button" class="btn btn-info">Show Query</button>
</div>
</form>
'''
print form
query = 'select *  from Plants'
def extendQuery(query,text):
  if 'where' in query:
    query+=' and '+text
  else:
    query+=' where '+text
  return query

if Name: 
  query = extendQuery(query,"Name = %d " % str(Name) )
if AssetDescription: 
  query = extendQuery(query,"AssetDescription = %f " % str(AssetDescription) )
if AssetType: 
  query = extendQuery(query,"AssetType = '%s' " % str(AssetType) )
if AssetID: 
  query = extendQuery(query,"AssetID = '%s' " % str(AssetID))
if FuelType: 
  query = extendQuery(query,"FuelType = %s " % str(FuelType))
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
           str(row['AssetID']),
           row['NormalCapacity'],
           row['CurrentCapacity'],
           str(row['FuelType']),
))
rows = d


hanger.bootstrap_table(rows,cols)
hanger.close()
