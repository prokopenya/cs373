from robot import *


def run(param1, param2):
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 100

    prev_y = myrobot.y
    for i in range(N):
        steer = - param1 * myrobot.y - param2 * (myrobot.y - prev_y)
        prev_y = myrobot.y
        myrobot = myrobot.move(steer, speed)
        print myrobot, steer
run(0.3, 3.0) # call function with parameter tau of 0.1 and print results
