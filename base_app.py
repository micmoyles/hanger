#!/usr/bin/python
import socket
import datetime as dt
import struct
import sys,log,os
from apx_test import XmlDictConfig
import xml.etree.ElementTree

class EApp:
    def __init__(self, name):
        self.name = name
        log.info('Starting... %s' % (self.name))
	self.launchtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class loader(EApp):
        # this needs to parse the XML file and upload it to the database
    def __init__(self,name,root_directory,database_host):
        EApp.__init__(self,name)
	self.root_directory = root_directory
        self.db = database_host
        self.timeout = 2.0
        assert os.path.exists(self.root_directory),'Could not find root directory, not continuing'
        
    def _parse(self,xmlfile):
        xmlfile = str(self.root_directory) + '/' + str(xmlfile)
        tree = xml.etree.ElementTree.parse(xmlfile)
        root = tree.getroot()
        msg = XmlDictConfig(root)
        if msg['flow'] != 'FREQ':
           continue
        SF = msg['msg']['row']['SF'] 
        TS = msg['msg']['row']['TS'] 
        TS = TS.strip(':GMT')
        cmd = 'insert into frequency vales ( %s , %d ) ' % (str(TS), SF) 
	

    def get_file(self):
        file_list = os.listdir(self.root_directory)
        this_file = sorted(file_list)[0] #choose newest file
	log.info(this_file)
        return this_file
	
    def __start__(self):
        while True:
            self._parse(self.get_file())
            sleep(self.timeout)
            

#class middleMan(talker):
## this will open a tcp socket and listen to commands from the GUI
#    def __init__(self, name):
#        talker.__init__(self,name)      
#
#class msg_loader(talker):
## this will listen to all messages and load the relevant ones to the hanger 
#    def __init__(self, name):
#        talker.__init__(self,name)      

