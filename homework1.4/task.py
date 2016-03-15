colors =      [['green', 'green', 'green'],
               ['green', 'red', 'green'],
               ['green', 'green', 'green']]

measurements = ['green', 'green', 'green' ,'green', 'green']

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

#-----------------------


def show(p):
    for i in range(len(p)):
        print p[i]

def calculate():

    W = len(colors[0]) #columns
    H = len(colors)    #rows

    def sense(p, Z):
        q = []
        for r in range(H):
            l = []
            for c in range(W):
                hit = (Z == colors[r][c])   #corresponds to the color(true||false)
                #probability
                l.append(p[r][c] * (hit * sensor_right + (1 - hit) * (1 - sensor_right)))
            q.append(l)

        s = sum([sum(l) for l in q])
        #normalize
        for r in range(H):
            for c in range(W):
                q[r][c] = q[r][c] / s

        return q

    def move(p, U):
        q = []
        for r in range(H):
            l = []
            for c in range(W):
                s = p_move * p[(r - U[0]) % H][(c - U[1]) % W]
                s += (1 - p_move) * p[r][c]

                l.append(s)
            q.append(l)

        return q

    #uniform distribution
    p = [[(1.0/(H*W))] * W] * H

    #Your probability array must be printed
    #with the following code.

    for Z, U in zip(measurements, motions):
        p = move(p, U)
        p = sense(p, Z)

    show(p)
    return p

calculate()
