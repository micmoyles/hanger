#!/usr/bin/python 

#script to hold common hanger functions

user = 'reader'
password = '1canR3ad'
#host = '54.194.208.88'
host = 'localhost'


def menu():
	menu = ''
	menu += str('<a href=dashboard.py><button type="button" class="btn btn-default btn-small">  Dashboard </button> </a> ')
	menu += str('<a href=trades.py><button type="button" class="btn btn-default btn-small">  Trades </button> </a> ')
	menu += str('<a href=trade_report.py><button type="button" class="btn btn-default btn-small">  Trade Reporting </button> </a> ')
	menu += str('<a href=energy_positions.py> <button type="button" class="btn btn-default btn-small">Position </button></a> ')
	menu += str('<a href=outages.py>  <button type="button" class="btn btn-default btn-small"> Outages </button></a> ')
	menu += str('<a href=plants.py>  <button type="button" class="btn btn-default btn-small"> Plant Config </button></a> ')
	menu += str('<a class="remit-menu" > <button type="button" class="btn btn-default btn-small"> REMIT </button></a> ')
	menu += str('<a class="extend-menu" > <button type="button" class="btn btn-default btn-small"> Extra </button></a> ')
	print "<div class='col-md-2'>"
	print "</div>"
	print "<div class='col-md-8'>"
	print menu
	print "</div>"

	print "<div class='row container' style='font-size:18px' >"
	print "<div class='col-md-2'>"
	print "</div>"
	print "<div class='col-md-8 menu-remit'>"
	print str('<a href=frequency.py> <button type="button" class="btn btn-default btn-small">  System Frequency </button></a> ')
 	print str('<a href=soso_prints.py> <button type="button" class="btn btn-default btn-small">  SO-SO Prints </button></a> ')
	print str('<a href=outages.py>  <button type="button" class="btn btn-default btn-small"> Outages </button></a> ')
	print str('<a href=canvas.py> <button type="button" class="btn btn-default btn-small">Live Charts </button></a> ')
	print str('<a href=plants.py>  <button type="button" class="btn btn-default btn-small"> Plant Config </button></a> ')
	print str('<a href=REMIT > <button type="button" class="btn btn-default btn-small"> Messages</button> </a> ')
	print "</div>"
	print "</div>"

	print "<div class='row container' style='font-size:18px' >"
	print "<div class='col-md-2'>"
	print "</div>"
	print "<div class='col-md-8 menu-extension'>"
	print str('<a href=bootstrap_book.html> <button type="button" class="btn btn-default btn-small"> Book Viewer </button></a> ')
	print str('<a href=charts.html> <button type="button" class="btn btn-default btn-small"> Trade Reconciliation</button> </a> ')
	print str('<a href=loader.py> <button type="button" class="btn btn-default btn-small"> Loader</button> </a> ')
	print str('<a href=canvas.py> <button type="button" class="btn btn-default btn-small">Live Charts </button></a> ')
	print str('<a href=REMIT > <button type="button" class="btn btn-default btn-small"> Messages</button> </a> ')
	print "</div>"
	print "</div>"

def start(title, showMenu=True ):
	print 'Content-Type: text-html'
	print '\n' # new line needed to identify html header
	print '<html>'
	print '  <head>'
	print '    <meta charset="utf-8">'
	print '    <meta http-equiv="X-UA-Compatible" content="IE=edge">'
	print '    <meta name="viewport" content="width=device-width, initial-scale=1">'
	print '    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->'
	print '    <title> %s </title>' % str(title)
	print ''
	print '     <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>'
	print '    <!-- Bootstrap -->'
	print '    <link href="css/bootstrap.min.css" rel="stylesheet">'
	print '    <script src="http://canvasjs.com/assets/script/canvasjs.min.js"></script>'
        print '    <link rel="stylesheet" href="hanger.css" type="text/css"/ >'
	print ''
	print '    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->'
	print '    <!-- WARNING: Respond.js doesnt work if you view the page via file:// -->'
	print '    <!--[if lt IE 9]>'
	print '      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>'
	print '      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>'
	print '    <![endif]-->'
	print '  </head>'
	print "<a href=index.py> <img src='EE.jpg'class='img-responsive' alt='Responsive image' style='height:100px;width:100px'></a>"
#	print '  <body class="container">'
	print '  <body>'
	if showMenu: menu()

def close():
	print '''
	    <!-- jQuery (necessary for Bootstraps JavaScript plugins) -->
	     <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
	     <!-- Include all compiled plugins (below), or include individual files as needed -->
	     <script src="js/bootstrap.min.js"></script>
		   <script src="app.js"></script>
    		   <!--<script src="book.js"></script>-->
                   <script src="sortable.js"></script>
                   <script src="dashboard.js"></script>
	   </body>
	  </html>
	'''

def p(text):
	# print html paragraph
	print '<p>' + str(text) + '</p>'
def h1(text):
	print '<h1 class="container" >' + str(text) + '</h1>'
def h2(text):
	print '<h2 class="container" >' + str(text) + '</h2>'
def h3(text):
	print '<h3 class="container" >' + str(text) + '</h3>'
def br():
	print '<br>'
def showquery(text):
	# print html paragraph
	print '''
              <div class="container">
              <code class="sql">  %s  </code>
              </div>
	''' % str(text)

def bootstrap_table(rows, cols):
# Idea of this function is to display a html table
# nCols = length cols
# nrows = length rows
# Header = entries of cols

	print '''
<div class="container">
<table class="table table-striped table-hover sortable">
'''
	evenRow = False

	nCols = len(cols)
	print '<tr>'
	for col in cols: print '<th>' + str(col) + '</th>' 
	print '</tr>'

	for row in rows: 
                
                if 'FAILURE' in row:
                    print "<tr class=danger>"
		else:
                    print "<tr>" 
		for r in row:
			print '<td>' + str(r) + '</td>'
		print '</tr>'
	print '</table>'
	print '</div>'

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
