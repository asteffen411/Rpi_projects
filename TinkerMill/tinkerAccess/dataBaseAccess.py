#!/usr/bin/python
#
# dataBaseAccess.py

import sys
import os


#import serial
#import serial.tools.list_ports
#import time
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



#queryBadgeId('1234')
#else:
  #print(scanConfigPath+" not found")
  #sys.exit(1)

#serialPort = False
#for port in list(serial.tools.list_ports.comports()):
  #print "Raspberry Pi serial comport: "
  #for portinfo in port:
    #print "   "+portinfo
  #for cfgPortName in C_portName.split():
    #if port[0] == cfgPortName:
      #serialPort = port[0]
      #print ("\n   Found a serial port that matches portName %s as defined in scan.cfg" % str(cfgPortName) )

#if not serialPort:
  #print("Unable to find a serial port that matches description %s as defined in scan.cfg" % C_portName )
  #sys.exit()

#serialConnection = serial.Serial(serialPort, C_portSpeed)
#serialConnection.flushInput()
#serialConnection.flushOutput()

#def watchPort():

  #timerThread = False

  ## just sit here and scan badges and allow access as long as the server says ok
  #while True:
    #usercode =  serialConnection.readline().strip()[-11:-1]
    #print("usercode=",str(usercode) )

    ## if this is a server
    #if C_clientServer == "server":
      #print("I'm a server")
      #code = "server"

    ## if this is a client
    #if C_clientServer == "client":
      #print("I'm a client")
      #try:
        #url="%s/device/%s/code/%s" % ( C_server, C_deviceid, usercode)
        #print "url=",url
        ##code = requests.get(url)
        #code = ""
      #except ValueError:
        #print "Oppps! I could not get the url %s/device/%s/code/%s" % ( C_server, C_deviceid, usercode)
      ##code = ""

      ## if access was granted run the unlock binary
      #if code == "":
        #print("unlocking", C_unlockbin)
        #os.system( C_unlockbin)

        ## if there is a timer running already then stop it and
        ## start a new timer
        #if timerThread:
          #timerThread.cancel()

        #timerThread = threading.Timer(C_devicetimeout , logOut)
        #timerThread.start()

    ## log out the last scan data
    #print("Logging out")
    #time.sleep(2)
    #os.system( C_lockbin)
    #print("C_scantxt",C_scantxt)
    #print("usercode=%s, code=%s\n" % (usercode, code))
    
    ####outfile = open(C_scantxt, "w")
    ####outfile.write("%s,%s\n" % (usercode, code))
    ####outfile.close()
    #time.sleep(1)
  #print("Done with watchPort")


## log a user out after so long
#def logOut():
  #print("Logout called")

#d1 = threading.Thread(name='daemon', target=watchPort)
#d1.setDaemon(True)

#d1.start()


#while True:
  #time.sleep(1)
  #watchPort()
  ##print(".")


