# Carter McCauley | 3/6/2024 | Raza's Rover
#I'm gonna learn how this thing works, maybe make it sing Megalovania

#imports
import PicoAutonomousRobotics
from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
buggy = KitronikPicoRobotBuggy()
import machine
#Vars
#magalovania song
sansP = [294, 294, 587, 440, 415, 392, 349, 294, 330, 349, 262, 262, 587, 440, 415, 392, 349, 294, 330, 349, 246, 246, 587, 440, 415, 392, 349, 294, 330, 349]
sansR = [0.125, 0.125, 0.25, 0.345, 0.25, 0.25, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.25, 0.345, 0.25, 0.25, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.25, 0.345, 0.25, 0.25, 0.25, 0.125, 0.125, 0.125]
sans = [sansP,sansR]
hitAlready = False
#song function
def song(title):
    x=0
    while x < len(title[1]):
        buggy.soundFrequency(title[0][x])
        sleep(title[1][x])
        x += 1
    buggy.silence()

#code
while True:
    if(buggy.button.value() == True):
        buggy.motorOn("l","f",20)
        buggy.motorOn("r","r",20)
        song(sans)
        buggy.motorOff("l")
        buggy.motorOff("r")


