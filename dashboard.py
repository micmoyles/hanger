#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import hanger

hanger.start('DashBoard' )
# Print container to hold doughnut chart
print '''
<br>
<div class='row container'>
<div class='col-md-6'>
<div id="doughnutChartContainer" style="height: 300px; width: 100%;"></div>
</div>
<div class='col-md-6'>
<div id="lineChartContainer" style="height: 300px; width: 100%;"></div>
</div>
<div class='col-md-6'>
</div>
'''
hanger.close()
