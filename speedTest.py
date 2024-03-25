import PicoAutonomousRobotics
from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
import machine
buggy = KitronikPicoRobotBuggy()
on = True
sleep(10)
while on == True:
    buggy.motorOn("l","f",50)
    buggy.motorOn("r","f",50)
    sleep(2)
    buggy.motorOn("l","f",100)
    buggy.motorOn("r","f",100)
    sleep(2)
    buggy.motorOn("l","f",1)
    buggy.motorOn("r","f",1)
    sleep(2)
    if(buggy.button.value() == True):
        on = False
buggy.motorOff("l")
buggy.motorOff("r")
    