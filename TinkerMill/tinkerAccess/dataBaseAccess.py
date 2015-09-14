#!/usr/bin/python
#  Andrew Steffen
#  Initial first pass attempt completed and working.
#  TOOO:  Verify other server side data exchanges will work.
#  TODO:  Add code comments and clean-up
# dataBaseAccess.py

import sys
<<<<<<< HEAD
=======
import os


>>>>>>> 94087b2eb572456c755c5a55326d3fc4035f43e2
import ConfigParser
import os
import requests


def queryUserNameFromBadgeId(badgeId):
  c = ConfigParser.SafeConfigParser()
  scanConfigPath=os.getcwd()+"/scan.cfg"

  if os.path.isfile(scanConfigPath):
    c.read(scanConfigPath)
    C_server    = c.get('config', 'server')
    C_deviceid  = c.get('config', 'deviceid')
    userData = 'NoUser'
    try:
      url="%s/user/code/%s" % ( C_server, badgeId )
      print "url=",url
      userData = requests.get(url)
      print("request returned ",userData.text )
      
    except ValueError:
      print "Oppps! I could not get the url %s/device/%s/code/%s" % ( C_server, C_deviceid, usercode)
    return userData  

<<<<<<< HEAD

def queryUserAccessLevel(userName):
  c = ConfigParser.SafeConfigParser()
  scanConfigPath=os.getcwd()+"/scan.cfg"

  if os.path.isfile(scanConfigPath):
    c.read(scanConfigPath)
    C_server    = c.get('config', 'server')
    C_deviceid  = c.get('config', 'deviceid')
    accessLevel = 'NoUser'
    try:
      url="%s/user/%s/device/C_deviceid" % ( C_server, userName )
      print "url=",url
      accessLevel = requests.get(url)
      print("request returned ",accessLevel.text )
      
    except ValueError:
      print "Oppps! I could not get the url %s/device/%s/code/%s" % ( C_server, C_deviceid, usercode)
    return accessLevel  



=======
>>>>>>> 94087b2eb572456c755c5a55326d3fc4035f43e2
