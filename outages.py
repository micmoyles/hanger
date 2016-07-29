#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
import datetime
#form = cgi.FieldStorage()
form = cgi.SvFormContentDict()
EventStatus	  = form.get('EventStatus', '')
AssetType	  = form.get('AssetType', '')
AffectedUnit 	  = form.get('AffectedUnit', '')
AssetID 	  = form.get('AssetID', '')
EventType         = form.get('EventType', '')
FuelType          = form.get('FuelType', '')
showForm          = form.get('showForm', '')
MessageHeading    = form.get('MessageHeading', '')
sql 	  = form.get('sql', '')

session = 'REMIT'
rangeInDays = 2
db = mdb.connect( hanger.host, hanger.user, hanger.password )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
hanger.start('REMIT Events')
hanger.h2('Current REMIT Events')
viewAll = '''
<div class=container>
<a href=outages.py?showForm=True>View all events here<a>
</div>
'''
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
<button type="submit" class="btn btn-default">Submit</button>
<button type="button" class="btn btn-info">Show Query</button>
</div>
</form>
'''
if showForm: print form
now = datetime.datetime.now().strftime( '%Y-%m-%d %H:%m:%S')
t1 = (datetime.datetime.now() - datetime.timedelta(days=rangeInDays)).strftime( '%Y-%m-%d %H:%m:%S') 
t2 = (datetime.datetime.now() + datetime.timedelta(days=rangeInDays)).strftime( '%Y-%m-%d %H:%m:%S') 
if not showForm: 
   query = "select EventStart,EventEnd,AssetID,EventType,NormalCapacity,AvailableCapacity  from outages where EventStart < ' %s ' and EventEnd > ' %s ' and EventStatus = 'OPEN'" % ( now, now) 
else:
   query = "select * from outages where EventStart > '%s' and EventEnd < '%s'" % ( t1, t2) 
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
if any((EventStatus,AffectedUnit,EventType,AssetID,MessageHeading)): showForm = True

cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
#cols = ['AffectedUnitEIC','AssetType','AffectedUnit','DurationUncertainty','RelatedInformation','AssetId','EventType','NormalCapacity','AvailableCapacity','EventStatus','EventStart','EventEnd','Cause','FuelType','Participant_MarketParticipantID','MassageHeading']
#cols = ['AffectedUnit','AssetId','EventType','NormCap','AvailCap','EventStatus','EventStart','EventEnd','FuelType','MessageHeading']
cols = ['EventStart','EventEnd','AssetID','EventType','NormCap','AvailCap']
rows = cursor.fetchall()
cursor.close()
d = []
for row in rows:
  d.append(( 
           str(row['EventStart']),
           str(row['EventEnd']),
           str(row['AssetId']),
           str(row['EventType']),
           row['NormalCapacity'],
           row['AvailableCapacity'],
))
rows = d


hanger.bootstrap_table(rows,cols)
print viewAll
hanger.close()
