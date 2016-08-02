#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
import MySQLdb as mdb
form = cgi.SvFormContentDict()
AssetType	  = form.get('AssetType', '')
AssetID 	  = form.get('AssetID', '')
FuelType          = form.get('FuelType', '')
Name              = form.get('Name', '')
AssetDescription  = form.get('AssetDescription','')
sql 	  = form.get('sql', '')
add_NormalCapacity	  = form.get('add_NormalCapacity', '')
add_AvailableCapacity	  = form.get('add_AvailableCapacity', '')
add_AssetID 	  = form.get('add_AssetID', '')
add_FuelType          = form.get('add_FuelType', '')
add_Name              = form.get('add_Name', '')

session = 'config'
db = mdb.connect( hanger.host, hanger.user, hanger.password )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use %s" % session )
hanger.start('Plant Config')
hanger.h2('Plant Config')
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
<button type="button" class="btn btn-sql btn-info">Show Query</button>
<button type="button" class="btn btn-info btn-addPlant">Add Plant</button>
</div>
</form>
'''
print form
query = '''
	select p.Name as Name, 
	p.AssetID as AssetID,
	p.FuelType as FuelType,
	p.NormalCapacity as NormCap, 
	ps.Status as Status,
	ps.CurrentCapacity as AvailCap
	from Plants p
	inner join plant_status ps on ps.AssetID = p.AssetID
'''

def extendQuery(query,text):
  if 'where' in query:
    query+=' and '+text
  else:
    query+=' where '+text
  return query

if Name: 
  query = extendQuery(query,"p.Name = '%s' " % str(Name) )
if AssetDescription: 
  query = extendQuery(query,"p.AssetDescription = '%s' " % str(AssetDescription) )
if AssetType: 
  query = extendQuery(query,"p.AssetType = '%s' " % str(AssetType) )
if AssetID: 
  query = extendQuery(query,"p.AssetID = '%s' " % str(AssetID))
if FuelType: 
  query = extendQuery(query,"p.FuelType = '%s' " % str(FuelType))
hanger.showquery(query)
if sql: 
  hanger.showquery(query)

cursor.execute(query)
cols = map(lambda x: x[0], cursor.description) 
cols = ['Name', 'AssetID', 'FuelType', 'Status', 'NormalCapacity','CurrentCapacity']
rows = cursor.fetchall()
d = []
for row in rows:
  d.append((str(row['Name']), 
           str(row['AssetID']),
           str(row['FuelType']),
           str(row['Status']),
           row['NormCap'],
           row['AvailCap'],
))
rows = d
hanger.bootstrap_table(rows,cols)


form = '''
<form class="form-inline container" method = "get" >
<div class="form-group">
<table class="table table-bordered">
    <tbody>
        <tr>
        <td>
        <label for="exampleInputName2">Name</label>
        <input type="text" name="add_Name" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Asset ID</label>
        <input type="text" name="add_AssetID" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Fuel Type</label>
        <input type="text" name="add_FuelType" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Normal Capacity</label>
        <input type="text" name="add_NormalCapacity" class="form-control" id="exampleInputName2">
        </td>
        <td>
        <label for="exampleInputName2">Available Capacity</label>
        <input type="text" name="add_AvailableCapacity" class="form-control" id="exampleInputName2">
        </td>
    </tbody>
</table>
<button type="addPlant" class="btn btn-default">Add Plant</button>
<button type="button" class="btn btn-info">Show Query</button>
</div>
</form>
'''
print "<div class='addPlant'>"
hanger.h3('Add Plant')
print form
if add_Name and add_AssetID and add_FuelType and add_NormalCapacity:
   if not add_AvailableCapacity:
       add_AvailableCapacity = add_NormalCapacity
   insert_query = "insert into Plants values ( '%s', '%s', '%s', %d )" % ( str(add_Name), str(add_AssetID), str(add_FuelType), float(add_NormalCapacity))
   cursor.execute(insert_query)
   insert_query = "insert into plant_status values ( '%s', '%s', %d, %d )" % ( str(add_AssetID), 'OPEN' , float(add_NormalCapacity), float(add_AvailableCapacity))
   cursor.execute(insert_query)
   db.commit()
else:
   insert_query = 'Missing Values so query is null'
hanger.showquery(insert_query)
print '</div>'
cursor.close()
hanger.close()
