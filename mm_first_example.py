#!/usr/bin/python 

import cgi, cgitb; cgitb.enable()
import time
form = cgi.FieldStorage()
data = form.getfirst('mydata')
name  = form.getfirst('name')
print 'Content-Type: text/html'
print '\n'

print '<html>'
print '<head>'
print '</head>'
print '<body>'
print '<p>'
print '\nHello ' + name + ' from Pi with data ' + data
print '\n' 
print form
print '</p>'
print '<h1>URL Generation</h1>'
for i in range(0,5): 
	print '<p>Sleeping....</p>'
	time.sleep(2)
print '<p><a href=http://pi/cgi-bin/old_view.py?mydata=Michael>Link</a> </p>'
print '</body>'
print '</html>'
