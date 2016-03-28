
from robot import *


def run(param):
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 100

    for i in range(N):
        steering = - param * myrobot.y
        myrobot = myrobot.move(steering, speed)
        print myrobot, steering

run(0.3) # call function with parameter tau of 0.1 and print results
