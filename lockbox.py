import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

lock = 2500
step1 = 2300
step2 = 2200
unlock = 2000

# ^ setup

while True:
    RPL.servoWrite(0,lock)
    print "Do you want to unlock a safe? Riddle me this:"
    print "Why don't you like sand?"

    p1 = raw_input("> ")
    if p1 == "course": # the correct password (in the right order) unlocks it a little bt
        RPL.servoWrite(0,step1) 
    else:
        RPL.servoWrite(0,lock) # the wrong password will relock the box and end further attempts
        print "It's over Anakin"
        break

    p2 = raw_input("> ")
    if p2 == "rough":
        RPL.servoWrite(0,step2)
    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        break


    p3 = raw_input("> ")
    if p3 == "irritating":
        RPL.servoWrite(0,unlock)
        print "General Kenobi, you are a bold one."
        break

    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        break
