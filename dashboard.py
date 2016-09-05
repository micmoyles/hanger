#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger

hanger.start('DashBoard' )
print '''
<br>
<div class='row container'>
<div class='col-md-6'>
<div id="doughnutChartContainer" style="height: 300px; width: 100%;"></div>
</div>
<div class='col-md-6'>
</div>
'''
hanger.close()
