import random
import numpy as np
     
def createmaze(size_maze):     
    sx = size_maze
    sy = size_maze
    dfs = [[0 for col in range(sx)] for row in range(sy)]
    maze = [[0 for col in range(2*sx+1)] for row in range(2*sy+1)]
    #1:up 2:down 3:left 4:right
    operation = {1:(0,-1),2:(0,1),3:(-1,0),4:(1,0)}
    direction = [1, 2, 3, 4]
    stack = []
     
    for i in range(2*sx+1):
        if i%2 == 0:
            for j in range(2*sx+1):
                maze[i][j] = 1
    for i in range(2*sy+1):
        if i%2 == 0:
            for j in range(2*sy+1):
                maze[j][i] = 1
     
    def generateMaze(start):
        x, y = start
        dfs[y][x] = 1
        random.shuffle(direction)
        for d in direction:
            px, py = (x + y for x, y in zip(start, operation[d]))
            if px < 0 or px >= sx or py < 0 or py >= sy:
                pass
            else:
                if dfs[py][px] is not 1:
                    mx = 2*x + 1
                    my = 2*y + 1
                    if d == 1:
                        maze[my-1][mx] = 0
                    elif d == 2:
                        maze[my+1][mx] = 0
                    elif d == 3:
                        maze[my][mx-1] = 0
                    elif d == 4:
                        maze[my][mx+1] = 0
                    generateMaze((px,py))        
     
    generateMaze((0,0))

    maze = np.array(maze)
    location = np.where(maze < 1)
    num = location[0].size
    point1 = np.random.randint(1,num)
    point2 = np.random.randint(1,num)
    while point2 == point1:
        point2 = np.random.randint(1,num)
    start = [location[0][point1],location[1][point1]]
    treasure = [location[0][point2],location[1][point2]]

    maze[treasure[0],treasure[1]] = 100
    maze[start[0],start[1]] = 10


    return maze













