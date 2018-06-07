# Welcome to Wall Evasion 2.0!
# This is wall evasion, with a bonus feature:
# will continue to turn for a minumum of .5s after a wall is no longer sensed

import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorL = 0
motorR = 2
right = 17
front = 16
left = 19
rgo = 2000
lgo = 200

# ^ all setup

RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorL, lgo) # start off both motors going straight
while True:
    RPL.servoWrite(motorR, rgo) # reset motors to straight through each loop
    RPL.servoWrite(motorL, lgo)

    while RPL.digitalRead(front) == 0: # something ahead, turn until nothing
        RPL.servoWrite(motorL, rgo) # turn left
        if RPL.digitalRead(left) == 0: # if something to the right, turn left
            RPL.servoWrite(motorL, lgo)
            RPL.servoWrite(motorR, lgo)
        if RPL.digitalRead(front) != 0: # nothing to front
            now = time.time()
            future = now + .5 # continue turning for an extra .5s
            while True:
                if time.time() > future:
                    RPL.servoWrite(motorR, rgo)
                    RPL.servoWrite(motorL, lgo)
                    break
            break

    while RPL.digitalRead(right) == 0: # something to right...
        RPL.servoWrite(motorL, rgo) # pivot
        if RPL.digitalRead(right) != 0: # nothing to side
            now = time.time()
            future = now + .5 # continue turning for an extra .5s
            while True:
                if time.time() > future:
                    RPL.servoWrite(motorR, rgo)
                    RPL.servoWrite(motorL, lgo)
                    break
            break

    while RPL.digitalRead(left) == 0: # something to left...
        RPL.servoWrite(motorR, lgo) # pivot
        if RPL.digitalRead(left) != 0: # nothing to side
            now = time.time()
            future = now + .5 # continue turning for an extra .5s
            while True:
                if time.time() > future:
                    RPL.servoWrite(motorR, rgo)
                    RPL.servoWrite(motorL, lgo)
                    break
            break
