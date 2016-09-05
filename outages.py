#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
import datetime
import log
#form = cgi.FieldStorage()
form = cgi.SvFormContentDict()
EventStatus	  = form.get('EventStatus', '')
AssetType	  = form.get('AssetType', '')
AffectedUnit 	  = form.get('AffectedUnit', '')
AssetID 	  = form.get('AssetID', '')
EventType         = form.get('EventType', '')
FuelType          = form.get('FuelType', '')
showForm          = form.get('showForm', '')
rangeInDays       = form.get('rangeInDays', '')
sql 	  = form.get('sql', '')
script = '''
<script type="text/javascript">
$(document).ready( function () {
        var dps = [];

var chart = new CanvasJS.Chart("plantProduction",{
        title :
                text: "Upcoming Production Profile"
        },
        axisX: {
                title: "Time"
        },
        axisY: {
                title: "GBP"
        },
        data: [{
                type: "line",
                dataPoints : dps
         }]
});
chart.render();

$.getJSON("/plant_data/TOTAL.json", function (data) {

    for (var i = 0; i < data.length; i++) {

      dps.push({ x: i, y: data[i].capacity });
                }

    chart.options.data[0].dps = dps;
    chart.render();
            });
});
</script>
'''

session = 'REMIT'
db = mdb.connect( hanger.host, hanger.user, hanger.password )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
hanger.start('REMIT Events')
hanger.h2('Current REMIT Events')
print('<div id="plantProduction" style="height: 300px; width: 100%;"></div>')
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
        <td>
        <label for="exampleInputName2">Range (Days)</label>
        <input type="text" name="rangeInDays" class="form-control" id="exampleInputName2">
        </td>
        </tr>
    </tbody>
</table>
<button type="submit" class="btn btn-default">Submit</button>
<button type="button" class="btn btn-info btn-sql">Show Query</button>
</div>
</form>
'''
if showForm: print form
now = datetime.datetime.now().strftime( '%Y-%m-%d %H:%m:%S')
log.info(rangeInDays)
if not rangeInDays: 
   rangeInDays=2
else:
   rangeInDays = int(rangeInDays)
t1 = (datetime.datetime.now() - datetime.timedelta(days=rangeInDays)).strftime( '%Y-%m-%d %H:%M:%S') 
t2 = (datetime.datetime.now() + datetime.timedelta(days=rangeInDays)).strftime( '%Y-%m-%d %H:%M:%S') 
if not showForm: 
   query = '''
	select messageCreationTs as ts,EventStart,EventEnd,AssetID,EventType,NormalCapacity,AvailableCapacity from outages 
	where EventStart < ' %s '
	 and EventEnd > ' %s ' 
	and EventStatus = 'OPEN' 
''' % ( now, now) 
else:
   query = "select messageCreationTs as ts,EventStart,EventEnd,AssetID,EventType,NormalCapacity,AvailableCapacity from outages where EventStart > '%s' and EventEnd < '%s'" % ( t1, t2) 
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
hanger.showquery(query)
if any((EventStatus,AffectedUnit,EventType,AssetID,rangeInDays)): showForm = True

cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
#cols = ['AffectedUnitEIC','AssetType','AffectedUnit','DurationUncertainty','RelatedInformation','AssetId','EventType','NormalCapacity','AvailableCapacity','EventStatus','EventStart','EventEnd','Cause','FuelType','Participant_MarketParticipantID','MassageHeading']
#cols = ['AffectedUnit','AssetId','EventType','NormCap','AvailCap','EventStatus','EventStart','EventEnd','FuelType','MessageHeading']
cols = ['messageTs','EventStart','EventEnd','AssetID','EventType','NormCap','AvailCap']
rows = cursor.fetchall()
cursor.close()
d = []
for row in rows:
  d.append(( 
           str(row['ts']),
           str(row['EventStart']),
           str(row['EventEnd']),
           "<a href=plant_detail.py?AssetID=%s> %s </a>" % ( str(row['AssetID']), str(row['AssetID']) ) ,
           str(row['EventType']),
           row['NormalCapacity'],
           row['AvailableCapacity'],
))
rows = d


hanger.bootstrap_table(rows,cols)
print viewAll
print script
hanger.close()
