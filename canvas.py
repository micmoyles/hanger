#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger

hanger.bootstrap_start('Charts')
hanger.h1('Charts')

print('<div id="chartContainer" style="height: 300px; width: 100%;"></div>')
print('</br>')
print('<div id="doughnutChartContainer" style="height: 300px; width: 100%;"></div>')

hanger.bootstrap_close()