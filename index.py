#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger

hanger.start('Home', showMenu=False)
print '''
<div class='container'>
<a href=dashboard.py><button type='button' class='btn btn-default btn-lg'>  DashBoard  </button></a>
<a href='http://54.194.208.88:3000'> <button type='button' class='btn btn-default btn-lg'> Grafana </button></a>
<a href='http://54.194.208.88:2812'> <button type='button' class='btn btn-default btn-lg'>  Monit  </button></a>
</div>
'''
hanger.close()
