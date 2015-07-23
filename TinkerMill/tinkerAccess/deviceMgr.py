#!/usr/bin/python
#
########################################################################
#   deviceMgr.py
#       Responsible for initializing tasks, starting threads,
#       and managing event calls between modules within the device.
#       
########################################################################

import thread
import RPi.GPIO as GPIO
import time
import lcdModule as LCD
import badgeScanModule as SCAN
import dataBaseAccess as DB

userName = "NOT IN USE"

########################################################################
#
########################################################################
def timerThread(threadName, delay):
    while 1:
        time.sleep(delay)
        #print "%s: %s" % (threadName, time.ctime(time.time()) )



########################################################################
#
########################################################################
def resetButtonThread(threadName, delay):
    while 1:
        time.sleep(delay)
        #print "%s: %s" % (threadName, time.ctime(time.time()) )

########################################################################
#
########################################################################
def lcdThread(threadName, delay):
    LCD.lcd_init()
    while 1:
        time.sleep(delay)
        #print "%s: %s" % (threadName, time.ctime(time.time()) )
        LCD.lcd_string(userName,LCD.LCD_LINE_1)
        LCD.lcd_string(time.ctime(time.time()),LCD.LCD_LINE_2)
    LCD.lcd_cleanup()

########################################################################
#   badgeScanThread
########################################################################
def badgeScanThread(threadName, delay):
    retcode = SCAN.scanInit()
    if retcode == "SUCCESS":
        print "%s: %s" % (threadName, time.ctime(time.time()) )
    else:
        print "FAILED ScanInit %s/n%s" % (retcode, time.ctime(time.time()) )
        #LCD.lcd_string(retcode,LCD.LCD_LINE_1)
        #LCD.lcd_string(time.ctime(time.time()),LCD.LCD_LINE_2)
        
    while 1:
        time.sleep(delay)
        userId = SCAN.watchPort()  # wait here until a badge is scanned
        userName = DB.queryBadgeId(userId)
        print "badgeScanThread %s: %s" % (userName.text, userId )



########################################################################
#
#   MAIN entry point
#
########################################################################
try:
    thread.start_new_thread(timerThread,("timer",10.0) )
    thread.start_new_thread(resetButtonThread,("resetButton",1.1) )
    thread.start_new_thread(lcdThread,("lcdThread",1.2) )
    thread.start_new_thread(badgeScanThread,("badgeScanThread",1.3) )
except:
    print "Error: unable to start thread"

while 1:
    pass


