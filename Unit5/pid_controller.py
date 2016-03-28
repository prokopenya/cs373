# -----------
# User Instructions
#
# Implement a P controller by running 100 iterations
# of robot motion. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau_p * CTE - tau_d * diff_CTE - tau_i * int_CTE
#
# where the integrated crosstrack error (int_CTE) is
# the sum of all the previous crosstrack errors.
# This term works to cancel out steering drift.
#
# Your code should print a list that looks just like
# the list shown in the video.
#
# Only modify code at the bottom!
# ------------

from robot import *



def run(param1, param2, param3):
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 100
    prev_y = myrobot.y
    sum_crosstrack_errors = 0

    myrobot.set_steering_drift(10.0 / 180.0 * pi) # 10 degree bias, this will be added in by the move function, you do not need to add it below!

    for i in range(N):
        # steering = -tau_p * CTE - tau_d * diff_CTE - tau_i * int_CTE
        steering = - param1 * myrobot.y - param2 * (myrobot.y - prev_y) - param3 * sum_crosstrack_errors
        sum_crosstrack_errors += myrobot.y
        prev_y = myrobot.y
        myrobot = myrobot.move(steering, speed)
        print myrobot


# Call your function with parameters of (0.2, 3.0, and 0.004)
run(0.2, 3.0, 0.004)
