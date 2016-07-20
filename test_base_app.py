#!/usr/bin/python

import base_app
x = base_app.loader('test1','/home/mmoyles/REMIT/','localhost')
x.username = 'root'
x.passwd = 'wiarreft'
x.__start__()
