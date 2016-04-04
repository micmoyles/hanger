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
        print "<link rel='stylesheet' href='/hanger.css' type='text/css'/ >"
	print '</head>'
	print '<body>'

def bootstrap_start():
	print 'Content-Type: text-html'
	print '\n' # new line needed to identify html header
	print '<html>'
	print '  <head>'
	print '    <meta charset="utf-8">'
	print '    <meta http-equiv="X-UA-Compatible" content="IE=edge">'
	print '    <meta name="viewport" content="width=device-width, initial-scale=1">'
	print '    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->'
	print '    <title>Bootstrap 101 Template</title>'
	print ''
	print '    <!-- Bootstrap -->'
	print '    <link href="css/bootstrap.min.css" rel="stylesheet">'
        print '    <link rel="stylesheet" href="/hanger.css" type="text/css"/ >'
	print ''
	print '    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->'
	print '    <!-- WARNING: Respond.js doesnt work if you view the page via file:// -->'
	print '    <!--[if lt IE 9]>'
	print '      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>'
	print '      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>'
	print '    <![endif]-->'
	print '  </head>'
	print '  <body>'

def bootstrap_close():
	print'    <!-- jQuery (necessary for Bootstraps JavaScript plugins) -->'
	print'    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>'
	print'    <!-- Include all compiled plugins (below), or include individual files as needed -->'
	print'    <script src="js/bootstrap.min.js"></script>'
	print'  </body>'
	print'</html>'

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




