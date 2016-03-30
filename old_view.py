#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
from hanger import *
form = cgi.FieldStorage()
data = form.getfirst('mydata')

h_start()
if not data:
	print '<p>No args found....exit</p>'
	print '<p>This means the script will stop executing now.</p>'
	sys.exit(0)
if data: print '<p> Hello ' + data + '</p>'
menu()
h_close()
