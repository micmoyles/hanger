#!/usr/bin/python
import socket
import datetime as dt
import struct
import sys,log,os
from apx_test import XmlDictConfig
import xml.etree.ElementTree
from time import sleep
import MySQLdb as mdb

class EApp:
    def __init__(self):
	self.launchtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class loader(EApp):
        # this needs to parse the XML file and upload it to the database
    def __init__(self,root_directory,database_host):
        EApp.__init__(self)
	self.root_directory = root_directory
        self.db = database_host
        self.sql = 'mysql'
        self.username = None
        self.passwd = None
        self.cleanup = True
        self.timeout = 2.0
        self.blacklist = []
        self.whitelist = []
        self.isBlack = False
        self.isWhite  = False
        assert os.path.exists(self.root_directory),'Could not find root directory, not continuing'
        
    def _parse(self,xmlfile):
        tree = xml.etree.ElementTree.parse(xmlfile)
        root = tree.getroot()
        msg = XmlDictConfig(root)
        log.info(msg)
        if 'flow' not in msg.keys(): return 0
        if msg['flow'] != 'FREQ':
           return 0
        SF = msg['msg']['row']['SF'] 
        TS = msg['msg']['row']['TS'] 
        TS = TS.strip(':GMT')
        db_cmd = 'use REMIT'
        if self.sql == 'mysql': load_cmd = 'insert ignore into frequency values ( " %s " , %f ) ' % (str(TS), float(SF) ) 
        log.info( load_cmd )
        db = mdb.connect( self.db, self.username , self.passwd )
        cursor = db.cursor(mdb.cursors.DictCursor)
        cursor.execute( db_cmd )
        cursor.execute( load_cmd )
        db.commit()
        cursor.close()
        return 0
	

    def get_file(self):
        file_list = os.listdir(self.root_directory)
        if len(file_list) == 0: return None
        this_file = sorted(file_list)[0] #choose newest file
	log.info(this_file)
        return str(self.root_directory) + '/' + str(this_file)

    def load_and_clear( self ):
        current_file = self.get_file()
        if current_file is None: return 
        self._parse( current_file )
        log.info( 'Deleting %s' % str( current_file ) ) 
        os.remove( current_file )
       
    def loadDirectory( self ):
        file_list = os.listdir( self.root_directory )
        for f in file_list:
            self._parse( str(self.root_directory) + '/' + f )
	
    def __start__(self):
        assert (self.username is not None) and (self.passwd is not None) and (self.db is not None), 'Loader needs username, password and host configured'
        assert (len(self.whitelist) != 0 ) and (len(self.backlist) != 0 ), "Cannot have a whitelist and a blacklist"
        if len(self.whitelist) != 0:
            self.isWhite = True
        if len(self.blacklist) != 0:
            self.isBlack = True
        log.info( self.__dict__ )
        while True:
            sleep( self.timeout )
            if self.cleanup: self.load_and_clear()
            else: self.loadDirectory()

