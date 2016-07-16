#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger

hanger.start('Charts')
hanger.h1('Charts')

print('<div id="chartContainer" style="height: 300px; width: 100%;"></div>')
print('<button type="button" class="btn btn-info btn-pause">Pause</button>')
print('<button type="button" class="btn btn-info btn-resume">Resume</button>')
print('</br>')
print('<div id="doughnutChartContainer" style="height: 300px; width: 100%;"></div>')

hanger.close()
