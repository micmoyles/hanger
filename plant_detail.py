#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
form = cgi.SvFormContentDict()
AssetID 	  = form.get('AssetID', '')
FuelType          = form.get('FuelType', '')
Name              = form.get('Name', '')
jsonData = '%s' % AssetID.upper()
script = '''
<script type="text/javascript">
$(document).ready( function () {
        var dps = [];

var chart = new CanvasJS.Chart("plantProduction",{
        title :{
                text: "Historical Book"
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

$.getJSON("/plant_data/%s.json", function (data) {

    for (var i = 0; i < data.length; i++) {

      dps.push({ x: i, y: data[i].capacity });
                }

    chart.options.data[0].dps = dps;
    chart.render();
            });
});
</script>
''' % jsonData 
db = mdb.connect( hanger.host, hanger.user, hanger.password )
cursor = db.cursor(mdb.cursors.DictCursor)
hanger.start('Plant %s' % AssetID)
hanger.h2('Plant Details - %s' % AssetID)
hanger.h3('<a href=plant_detail.py?AssetID=TOTAL> Show Total Capacity </a>')
#query = '''
#	select p.Name as Name, 
#	p.AssetID as AssetID,
#	p.FuelType as FuelType,
#	p.NormalCapacity as NormCap, 
#	ps.Status as Status,
#	ps.CurrentCapacity as AvailCap
#	from config.plants p
#	inner join config.plant_status ps on ps.AssetID = p.AssetID
#'''

query = '''
        select messageCreationTs as ts,EventStart,EventEnd,AssetID,EventType,NormalCapacity,AvailableCapacity from REMIT.outages 
        where AssetID = '%s'
''' % AssetID 
cursor.execute(query)
cols = ['Name', 'AssetID', 'FuelType', 'Status', 'NormalCapacity','CurrentCapacity']
cols = ['messageTs','EventStart','EventEnd','AssetID','EventType','NormCap','AvailCap']

rows = cursor.fetchall()
#d = []
#for row in rows:
#  d.append((str(row['Name']), 
#           str(row['AssetID']),
#           str(row['FuelType']),
#           str(row['Status']),
#           row['NormCap'],
#           row['AvailCap'],
#))
#rows = d
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

print('<div id="plantProduction" style="height: 300px; width: 100%;"></div>')

hanger.bootstrap_table(rows,cols)

cursor.close()

print script
hanger.close()
