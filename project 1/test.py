import maze
import solution
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--maze_size', type=int, default=10)

if __name__ == '__main__':
    args = parser.parse_args()
    time_cost = [0,0,0,0]
    node_num = [0,0,0,0]

    for i in range(1000):
        Maze = maze.createmaze(args.maze_size)
        while solution.solution_maze(Maze,'DFS') == False:
            Maze = maze.createmaze(args.maze_size)
        print('testing Maze  ' + str(i+1))
        time_start = time.time()
        Answer = solution.solution_maze(Maze,'DFS')
        time_end = time.time()
        time_cost[0] += time_end - time_start
        node_num[0] += len(Answer)
        time_start = time.time()
        Answer = solution.solution_maze(Maze,'BFS')
        time_end = time.time()
        time_cost[1] += time_end - time_start
        node_num[1] += len(Answer)
        time_start = time.time()
        Answer = solution.solution_maze(Maze,'uniform')
        time_end = time.time()
        time_cost[2] += time_end - time_start
        node_num[2] += len(Answer)
        time_start = time.time()
        Answer = solution.solution_maze(Maze,'A*')
        time_end = time.time()
        time_cost[3] += time_end - time_start
        node_num[3] += len(Answer)

    print('')
    print('Test Result')
    print('Maze_size = '+str(2*args.maze_size + 1))
    print('method:DFS   time_cost:' + str(time_cost[0]).zfill(5) + '  Average node: ' + str(node_num[0]/1000).zfill(7))
    print('method:BFS   time_cost:' + str(time_cost[1]).zfill(5) + '  Average node: ' + str(node_num[1]/1000).zfill(7))
    print('method:UCS   time_cost:' + str(time_cost[2]).zfill(5) + '  Average node: ' + str(node_num[2]/1000).zfill(7))
    print('method:A*S   time_cost:' + str(time_cost[3]).zfill(5) + '  Average node: ' + str(node_num[3]/1000).zfill(7))







