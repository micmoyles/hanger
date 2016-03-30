#!/usr/bin/python 

#script to hold common hanger functions

def menu():
	menu = ''
	menu += str('<div id=".menu-btn">  Menu </div>| ')
	menu += str('<a href=trades.py> Trades </a>| ')
	menu += str('<a href=position.py> Position </a>| ')
	menu += str('<a href=loader.py> Loader </a>| ')
	menu += str('<a href=messages.py> Messages </a>| ')
	menu += str('<a href=stats.py> Hanger Stats </a>| ')
	print menu

def h_start():
	print 'Content-Type: text/html'
	print '\n'
	print '<html>'
	print '<head>'
#	print "<style type='text/css'>"
#	print "body { font-size: 14pt;}"
#	print "table { font-size: 10pt; font-family: helvitica}"
#	print "tr.oddrowcolour{ background-color:#d4e3e5; }"
#	print "tr.evenrowcolour{ background-color:#c3dde0; }"
#	print '</style>'
        print "<link rel='stylesheet' href='/hanger.css' type='text/css'/ >"
	print '</head>'
	print '<body>'

def h_close():
	print '</body>'
	print '</html>'

def p(text):
	# print html paragraph
	print '<p>' + str(text) + '</p>'
def h1(text):
	print '<h1>' + str(text) + '</h1>'
def h2(text):
	print '<h2>' + str(text) + '</h2>'
def h3(text):
	print '<h3>' + str(text) + '</h3>'
def br():
	print '<br>'
def showquery(text):
	# print html paragraph
	print '<code>' + str(text) + '</code>'

def table(rows, cols):
# Idea of this function is to display a html table
# nCols = length cols
# nrows = length rows
# Header = entries of cols

	print '<table border="1" style="background-color:#FFFF99;border-collapse:collapse;border:1px solid #000033;color:#000000;width:90%" cellpadding="4" cellspacing="1"; align="center">'
	evenRow = False

	nCols = len(cols)
	print '<tr>'
	for col in cols: print '<th>' + str(col) + '</th>' 
	print '</tr>'

	for row in rows: 
		print "<tr class='oddrowcolour'>" if not evenRow else "<tr class='evenrowcolour' >"
		for r in row.values():
			print '<td>' + str(r) + '</td>'
		print '</tr>' if not evenRow else '</tr>'
		if evenRow: 
			evenRow = False
		elif not evenRow:
			evenRow = True
	print '</table>'




