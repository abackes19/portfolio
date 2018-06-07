# welcome to wall following !
# using analog and digital sensors, it will follow a wall


import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorL = 0
motorR = 2

right = 19
front = 16
left = 17
analogL = 1

rgo = 2000
lgo = 1000

# ^ setup

RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorL, lgo) # turn on both motors going straight

while True:
    RPL.servoWrite(motorR, rgo)
    RPL.servoWrite(motorL, lgo)

    while RPL.analogRead(analogL) >= 400: # middle range, can go straight
        RPL.servoWrite(motorR, rgo)
        RPL.servoWrite(motorL, lgo)

    while RPL.analogRead(analogL) < 400: # no longer middle
        if RPL.digitalRead(left) == 0: # digital also sense, so close
            RPL.servoWrite(motorR, 0) # turn away from wall
            RPL.servoWrite(motorL, lgo)

        if RPL.digitalRead(left) == 1: # digital doesn't sense, far
            RPL.servoWrite(motorR, rgo) # turn towards wall
            RPL.servoWrite(motorL, 0)
