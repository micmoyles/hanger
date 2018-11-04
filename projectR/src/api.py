#!/usr/bin/python
# pip install flask
# pip install flask-restful
from flask import Flask, request
from flask_restful import Resource, Api
import MySQLdb as mdb

app = Flask(__name__)
api = Api(app)
data = {}
getQuery = '''
	select name, dob from users where name = "%s"
''' 
db = mdb.connect( 'localhost', "reader", "1canR3ad" )
cursor = db.cursor(mdb.cursors.DictCursor)
cursor.execute( "use projectR" )

def getDaystoBirthday(birthday):
	return 10

class User(Resource):

	
	def get(self, name):

		query = getQuery % name
		cursor.execute( query )
		response = cursor.fetchone()
		print response
		
		if response['name'].lower() != name.lower():
			print 'Some kind of serious error'
			return 400
		return "Hello %s!, your birthday is in %d days" % (name,getDaystoBirthday(response['dob']))


	def put(self,name):

		try:
			json_data = request.get_json()
			dob = json_data['dob']
			data[name] = dob
			return 204

		except:
			return 400
		

# Create routes
api.add_resource(User, '/hello/<name>','/hello')

if __name__ == '__main__':
	#app.run(host='0.0.0.0', port=5000, debug=True)
	app.run(debug=True)