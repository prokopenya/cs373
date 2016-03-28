# -------------
# User Instructions
#
# Now you will be incorporating fixed points into
# your smoother.
#
# You will need to use the equations from gradient
# descent AND the new equations presented in the
# previous lecture to implement smoothing with
# fixed points.
#
# Your function should return the newpath that it
# calculates.
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
#
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *

# Do not modify path inside your function.
path=[[0, 0], #fix
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]

# Do not modify fix inside your function
fix = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

######################## ENTER CODE BELOW HERE #########################

def smooth(path, fix, weight_data = 0.0, weight_smooth = 0.1, tolerance = 0.00001):

    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    keep_smoothing = True
    prev_error = 10**9

    while keep_smoothing:
        error = 0.0
        for i in range(len(path)):
            if fix[i]:
                continue

            for j in range(len(path[i])):
                e1 = weight_data * (path[i][j] - newpath[i][j])
                newpath[i][j] += e1

                e2 = weight_smooth * (newpath[(i+1)%len(path)][j] \
                                    + newpath[(i-1)%len(path)][j] \
                                    - 2 * newpath[i][j])
                newpath[i][j] += e2

                e3 = (weight_smooth*0.5) * (2 * newpath[(i-1)%len(path)][j] \
                                              - newpath[(i-2)%len(path)][j] \
                                              - newpath[i][j])
                newpath[i][j] += e3

                e4 = (weight_smooth*0.5) * (2 * newpath[(i+1)%len(path)][j] \
                                              - newpath[(i+2)%len(path)][j] \
                                              - newpath[i][j])
                newpath[i][j] += e4

                error += abs(e1 + e2 + e3 + e4)

        if (prev_error - error) < tolerance:
            keep_smoothing = False
        else:
            prev_error = error

    return newpath 


#thank you - EnTerr - for posting this on our discussion forum

#newpath = smooth(path, fix)
#for i in range(len(path)):
