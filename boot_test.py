#!/usr/bin/python

import cgi, cgitb; cgitb.enable()
import sys
import hanger
hanger.bootstrap_start()
hanger.menu()
hanger.h1('Trades')
hanger.bootstrap_close()
