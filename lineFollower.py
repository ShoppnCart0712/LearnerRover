# Carter McCauley | 3/25/2024 | Raza's Rover
#line following

#imports
import PicoAutonomousRobotics
from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
import machine
buggy = KitronikPicoRobotBuggy()
on = False
baseline = buggy.getRawLFValue("c")
buggy.setLED(0,(0,255,0))
buggy.setLED(1,(0,255,0))
buggy.setBrightness(100)
buggy.show()
while True:
    if(buggy.button.value() == True):
        sleep(2)
        on = True
    """
    centreVal = buggy.getRawLFValue("c")
    leftVal = buggy.getRawLFValue("l")
    rightVal = buggy.getRawLFValue("r")
    print("Centre:", centreVal, " Left:",leftVal," Right:",rightVal)
    sleep(1)"""
    
    while (on == True):
        buggy.setLED(0,(255,255,255))
        buggy.setLED(1,(255,255,255))
        buggy.setBrightness(100)
        if abs(buggy.getRawLFValue("c") ) < 15000:
            buggy.motorOn("l","r",2)
            buggy.motorOn("r","f",2)
            buggy.setLED(0,(0,255,255))
            buggy.setLED(1,(0,255,255))
        elif (buggy.getRawLFValue("l")) < 15000:
            buggy.motorOff("r")
            buggy.motorOn("l","f",2)
            buggy.setLED(0,(0,255,255))
        elif (buggy.getRawLFValue("r")) < 15000:
            buggy.motorOff("l")
            buggy.motorOn("r","f",2)
            buggy.setLED(1,(0,255,255))
        else:
            buggy.motorOn("l","f",5)
            buggy.motorOn("r","f",5)
            buggy.setLED(0,(255,255,255))
            buggy.setLED(1,(255,255,255))
        buggy.show()
        sleep(0.1)
        buggy.motorOff("l")
        buggy.motorOff("r")
        sleep(0.1)
            
        if(buggy.button.value() == True):
            buggy.setLED(0,(0,0,0))
            buggy.setLED(1,(0,0,0))
            buggy.setBrightness(0)
            buggy.show()
            sleep(2)
            buggy.motorOff("l")
            buggy.motorOff("r")
            on = False