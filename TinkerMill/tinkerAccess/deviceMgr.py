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
def deviceAccessControlThread(threadName, delay):
    LOCK_PIN = 17
    a_lock.acquire(1)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LOCK_PIN, GPIO.OUT)  # E
    while 1:
        print "LOCK_PIN FALSE  %s: %s" % (threadName, time.ctime(time.time()) )
        GPIO.output(LOCK_PIN, False)
        a_lock.acquire()
        tstart=time.time()
        print "LOCK_PIN TRUE  %s: %s" % (threadName, time.ctime(tstart) )
        GPIO.output(LOCK_PIN, True)
        while (time.time() < delay+tstart):
          timeremaining = time.ctime((delay+tstart)-time.time() )[14:20]
          LCD.lcd_string(timeremaining,LCD.LCD_LINE_2)
          print "LOCK_PIN TRUE  %s: %s" % (threadName, timeremaining )
          time.sleep(0.5)
        LCD.lcd_string('WELCOME' ,LCD.LCD_LINE_1)
        LCD.lcd_string(time.ctime(time.time()) ,LCD.LCD_LINE_2)


########################################################################
#
########################################################################
def resetButtonThread(threadName, delay):
    RESET_PIN = 16
    resetPinVal = GPIO.LOW
    GPIO.setup(RESET_PIN, GPIO.IN)
    print "%s: %s" % (threadName, time.ctime(time.time()) )
    while 1:
        time.sleep(delay)
        resetPinVal = GPIO.input(RESET_PIN)
        #print "%s: %s %i" % ("RESETING pin", time.ctime(time.time()), resetPinVal )
        if resetPinVal == GPIO.HIGH:
            print "%s: %s %i" % ("RESETING", time.ctime(time.time()), resetPinVal )
            LCD.lcd_string("RESETTING",LCD.LCD_LINE_1)
            LCD.lcd_string(time.ctime(time.time()),LCD.LCD_LINE_2)
            a_lock.release()
            resetPinVal = GPIO.LOW
            


########################################################################
#
########################################################################
def startLCD():
    LCD.lcd_init()
    print "%s: %s" % ("WELCOME", time.ctime(time.time()) )
    LCD.lcd_string("WELCOME",LCD.LCD_LINE_1)
    LCD.lcd_string(time.ctime(time.time()),LCD.LCD_LINE_2)


########################################################################
#   badgeScanThread
########################################################################
def badgeScanThread(threadName, delay):
    retcode = SCAN.scanInit()
    if retcode == "SUCCESS":
        print "%s: %s" % (threadName, time.ctime(time.time()) )
    else:
        print "FAILED ScanInit %s/n%s" % (retcode, time.ctime(time.time()) )
        LCD.lcd_string(retcode,LCD.LCD_LINE_1)
        LCD.lcd_string(time.ctime(time.time()),LCD.LCD_LINE_2)
        
    while 1:
        time.sleep(delay)
        badgeId = SCAN.watchPort()  # wait here until a badge is scanned
        userName = DB.queryUserNameFromBadgeId(badgeId)
        print "badgeScanThread %s: %s" % (userName.text, badgeId )        
        LCD.lcd_string(userName.text,LCD.LCD_LINE_1)
        LCD.lcd_string(time.ctime(time.time()),LCD.LCD_LINE_2)
        a_lock.release()



########################################################################
#
#   MAIN entry point
#
########################################################################
try:
    a_lock = thread.allocate_lock()
    startLCD()
    resetButtonThreadID = thread.start_new_thread(resetButtonThread,("resetButton",0.5) )
    deviceAccessThreadID = thread.start_new_thread(deviceAccessControlThread,("deviceAccessControl",120.0) )
    badgeScanThreadID = thread.start_new_thread(badgeScanThread,("badgeScanThread",0.1) )
    

except:
    print "Error: unable to start thread"

while 1:
    pass


