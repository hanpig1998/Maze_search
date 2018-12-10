import numpy as np
import queue

class Maze_unit(object):
    def __init__(self, x, y, path_length, treasure_distance):
        self.x = x
        self.y = y
        self.h_n = path_length
        self.g_n = treasure_distance

    def __lt__(self, other):
        return self.h_n + self.g_n < other.h_n + other.g_n


def solution_maze(maze,method):
    maze_size = maze.shape[0]
    start = [np.where(maze==10)[0][0],np.where(maze==10)[1][0]]
    treasure = [np.where(maze==100)[0][0],np.where(maze==100)[1][0]]
    solution = []
    visited = np.zeros([maze_size,maze_size])
    distance = np.zeros([maze_size,maze_size])
    for i in range(maze_size):
        for j in range(maze_size):
            distance[i][j] = abs(i-treasure[0]) + abs(j-treasure[1])

    if method == 'DFS':
        stack = []
        stack.append([start[0],start[1]])
        while stack:
            temp = stack.pop()
            solution.append([temp[0],temp[1]])
            visited[temp[0],temp[1]] = 1
            if temp[0] == treasure[0] and temp[1] == treasure[1]:
                return solution
            if visited[temp[0]-1,temp[1]] == 0 and maze[temp[0]-1,temp[1]] != 1:
                stack.append([temp[0]-1,temp[1]])
            if visited[temp[0]+1,temp[1]] == 0 and maze[temp[0]+1,temp[1]] != 1:
                stack.append([temp[0]+1,temp[1]])
            if visited[temp[0],temp[1]-1] == 0 and maze[temp[0],temp[1]-1] != 1:
                stack.append([temp[0],temp[1]-1])
            if visited[temp[0],temp[1]+1] == 0 and maze[temp[0],temp[1]+1] != 1:
                stack.append([temp[0],temp[1]+1])

        return False
    elif method == 'BFS':
        q = queue.Queue()
        q.put([start[0],start[1]])
        while q:
            temp = q.get()
            solution.append([temp[0],temp[1]])
            visited[temp[0],temp[1]] = 1
            if temp[0] == treasure[0] and temp[1] == treasure[1]:
                return solution
            if visited[temp[0]-1,temp[1]] == 0 and maze[temp[0]-1,temp[1]] != 1:
                q.put([temp[0]-1,temp[1]])
            if visited[temp[0]+1,temp[1]] == 0 and maze[temp[0]+1,temp[1]] != 1:
                q.put([temp[0]+1,temp[1]])
            if visited[temp[0],temp[1]-1] == 0 and maze[temp[0],temp[1]-1] != 1:
                q.put([temp[0],temp[1]-1])
            if visited[temp[0],temp[1]+1] == 0 and maze[temp[0],temp[1]+1] != 1:
                q.put([temp[0],temp[1]+1])

        return False

    elif method == 'A*':
        q = queue.PriorityQueue()
        temp = Maze_unit(start[0], start[1] ,0, distance[start[0],start[1]])
        q.put(temp)
        while q:
            temp = q.get()
            solution.append([temp.x,temp.y])
            visited[temp.x,temp.y] = 1
            if temp.x == treasure[0] and temp.y == treasure[1]:
                return solution
            if visited[temp.x-1,temp.y] == 0 and maze[temp.x-1,temp.y] != 1:
                temp_lx = Maze_unit(temp.x-1, temp.y, temp.h_n+1, distance[temp.x-1,temp.y])
                q.put(temp_lx)

            if visited[temp.x+1,temp.y] == 0 and maze[temp.x+1,temp.y] != 1:
                temp_rx = Maze_unit(temp.x+1, temp.y, temp.h_n+1, distance[temp.x+1,temp.y])
                q.put(temp_rx)

            if visited[temp.x,temp.y-1] == 0 and maze[temp.x,temp.y-1] != 1:
                temp_uy = Maze_unit(temp.x, temp.y-1, temp.h_n+1, distance[temp.x,temp.y-1])
                q.put(temp_uy)

            if visited[temp.x,temp.y+1] == 0 and maze[temp.x,temp.y+1] != 1:
                temp_dy = Maze_unit(temp.x, temp.y+1, temp.h_n+1, distance[temp.x,temp.y+1])
                q.put(temp_dy)

        return False















