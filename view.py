#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
form = cgi.FieldStorage()
data = form.getfirst('mydata')

def menu():
#	menu = [] 
#	menu.append('Test 1 | ')
#	menu.append('Test 2 | ')
	menu = ''
	menu += str('Test 1 | ')
	menu += str('Test 2 | ')
	print menu

#print '\nHello ' + data
#print '\n' 
#print form

print 'Content-Type: text/html'
print '\n'
print '<html>'
print '<head>'
print '</head>'
print '<body>'
print '<p> Hello ' + data + '</p>'
menu()
print '</body>'
print '</html>'
