# tinkerAccess
Written by Andrew Steffen, asteffen411@gmail.com

DESIGN BACKGROUND:
------------------
TinkerMill provides access to many machines such as Laser cutters,
wood lathe, end mills, 3d printers, table saws, blacksmith furnace
and more.  Members are required to go through a safety course/training
on most machines before using.  Since TinkerMill's membership has grown,
it is hard to keep track of each member's training log.  Ideally,
tinkerMill could use the existing member badges to authorize a member 
access to a specific machine.  

A low cost design solution has been proposed to use a RaspberryPi
micro-controller and a badge access device scanner.  The idea is to have 
a RPi device scanner (client) at each machine and one Rpi server.  If a 
tinkerMill member wishes to use a machine, they scan their badge and
the RPi checks with the RPi server to see if that member is authorized 
to use that machine.  If they are authorized, the RPi scanner/client
will send an electronic signal indicating permission to use the machine.
This electric signal could be a simple LED light, a relay switch, or 
energized soleniod.  Also after authorization, the Rpi client sets 
an access authorized timer for limiting the maximum amount of time for
the machine to be used.  If the member finishes using the equipment, 
there will be a reset button to allow them to effectively logoff the 
machine.





CHANGE HISTORY LOG NOTES:
-------------------------
July 22:
Started with code from https://github.com/TinkerMill/tinkerAccess
1) Changed scan.py to deviceMgr.py.
2) Modify device.py so that it is kicking off multiple threads.
    Try to keeo things modular so that others can easily maintain it.
    Break up the design into smaller modules/files
      Over all device system management and coordination of activities.
      LCD screen.
      Badge scanning and access.
      Database accessing.
      Global device configuration settings (original scan.cfg file).
      
    Initial thought of threads needed are:
      Timer expiration
      Reset button
      LCD displaying messages
      Badge scanning
    
    There probably is too many threads.  
    This first attempt is isolate each module and look at behavior
    independently.  

July 23:
1) Need to get changes committed to github.  
