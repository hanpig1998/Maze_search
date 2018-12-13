import maze
import solution
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--maze_size', type=int, default=10)

if __name__ == '__main__':
    args = parser.parse_args()
    time_cost = [0,0,0,0]
    opennum = [0,0,0,0]
    closenum = [0,0,0,0]
    pathcost = [0,0,0,0]

    for i in range(1000):
        Maze = maze.createmaze(args.maze_size)
        while solution.solution_maze(Maze,'DFS') == False:
            Maze = maze.createmaze(args.maze_size)
        print('testing Maze  ' + str(i+1))
        time_start = time.time()
        a,open1,close1,pathcost1 = solution.solution_maze(Maze,'DFS')
        time_end = time.time()
        time_cost[0] += time_end - time_start
        opennum[0] += open1
        closenum[0] += close1
        pathcost[0] += pathcost1

        time_start = time.time()
        a,open1,close1,pathcost1 = solution.solution_maze(Maze,'BFS')
        time_end = time.time()
        time_cost[1] += time_end - time_start
        opennum[1] += open1
        closenum[1] += close1
        pathcost[1] += pathcost1

        time_start = time.time()
        a,open1,close1,pathcost1 = solution.solution_maze(Maze,'uniform')
        time_end = time.time()
        time_cost[2] += time_end - time_start
        opennum[2] += open1
        closenum[2] += close1
        pathcost[2] += pathcost1

        time_start = time.time()
        a,open1,close1,pathcost1 = solution.solution_maze(Maze,'A*')
        time_end = time.time()
        time_cost[3] += time_end - time_start
        opennum[3] += open1
        closenum[3] += close1
        pathcost[3] += pathcost1



        
    print('')
    print('Test Result')
    print('Maze_size = '+str(2*args.maze_size + 1))
    print('method:DFS   time_cost:' + str(round(time_cost[0], 2)) + '  Average openlist: '
     + str(opennum[0]/1000) + '  Average closelist: ' + str(closenum[0]/1000) + '  Average pathcost: ' + str(pathcost[0]/1000))
    print('method:BFS   time_cost:' + str(round(time_cost[1], 2)) + '  Average openlist: '
     + str(opennum[1]/1000) + '  Average closelist: ' + str(closenum[1]/1000) + '  Average pathcost: ' + str(pathcost[1]/1000))
    print('method:UCS   time_cost:' + str(round(time_cost[2], 2)) + '  Average openlist: '
     + str(opennum[2]/1000) + '  Average closelist: ' + str(closenum[3]/1000) + '  Average pathcost: ' + str(pathcost[2]/1000))
    print('method:Astar time_cost:' + str(round(time_cost[3], 2)) + '  Average openlist: '
     + str(opennum[3]/1000) + '  Average closelist: ' + str(closenum[3]/1000) + '  Average pathcost: ' + str(pathcost[3]/1000))







