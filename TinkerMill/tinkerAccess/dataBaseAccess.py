#!/usr/bin/python
#  Andrew Steffen
#  Initial first pass attempt completed and working.
#  TOOO:  Verify other server side data exchanges will work.
#  TODO:  Add code comments and clean-up
# dataBaseAccess.py

import sys
import os


import ConfigParser
import os
import requests


def queryBadgeId(badgeId):
  c = ConfigParser.SafeConfigParser()
  scanConfigPath=os.getcwd()+"/scan.cfg"

  if os.path.isfile(scanConfigPath):
    c.read(scanConfigPath)
    C_server    = c.get('config', 'server')
    C_deviceid  = c.get('config', 'deviceid')
    userData = 'NoUser'
    try:
      url="%s" % ( C_server )
      print "url=",url
      userData = requests.get(url)
      print("request returned ",userData.text )
      
    except ValueError:
      print "Oppps! I could not get the url %s/device/%s/code/%s" % ( C_server, C_deviceid, usercode)
    return userData  

