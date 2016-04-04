import segmented_cte as task

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def main(grid, init, goal, steering_noise, distance_noise, measurement_noise,
     weight_data, weight_smooth, p_gain, d_gain):
    path = task.plan(grid, init, goal)
    path.astar()
    path.smooth(weight_data, weight_smooth)

    x_spath = [dot[0] for dot in path.spath]
    y_spath = [dot[1] for dot in path.spath]

    reach_goal, num_collisions, num_steps, rpath, measurements = task.run(grid, goal, path.spath, [p_gain, d_gain])

    x_rpath = [dot[0] for dot in rpath]
    y_rpath = [dot[1] for dot in rpath]

    x_ms = [dot[0] for dot in measurements]
    y_ms = [dot[1] for dot in measurements]

    # ----------------------------------------
    # draw paths

    plt.figure()
    plt.plot(x_spath, y_spath, 'k-', x_spath, y_spath, 'ko', \
             x_rpath, y_rpath, 'b-', x_rpath, y_rpath, 'bo', \
             x_ms, y_ms, 'rx')

    # ----------------------------------------
    # draw obstacles

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                cir = Circle( (x, y), radius=0.5)
                plt.gca().add_patch(cir)

    plt.axis([-0.5, len(grid) - 0.5, -0.5, len(grid[0]) - 0.5])

    plt.show()

    return reach_goal, num_collisions, num_steps


# ------------------------------------------------
#
# input data and parameters
#


# grid format:
#   0 = navigable space
#   1 = occupied space

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0]]


init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]


steering_noise    = 0.1
distance_noise    = 0.03
measurement_noise = 0.3

weight_data       = 0.1
weight_smooth     = 0.2
p_gain            = 2.0
d_gain            = 6.0


print main(grid, init, goal, steering_noise, distance_noise, measurement_noise,
           weight_data, weight_smooth, p_gain, d_gain)
