import pygame
import sys
from pygame.locals import *
import traceback
import people
import wall
import random
import numpy as np
import maze
import solution


pygame.init()
pygame.mixer.init()
size = width,height = 960,672
bg = (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze")
back = (0,0,0)
level = 1;
pygame.mixer.music.load("music.ogg")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1) 


def main():
    clock = pygame.time.Clock()
    Gamestate = 0

    text_font = pygame.font.Font('font/avqest.ttf',64)
    text_startmenu = text_font.render(u'Caveman and treasure', True, (255,255,255))
    text_startmenu_rect = text_startmenu.get_rect()
    text_startmenu_rect.center = (width/2,height/2) 
    text_nextlevel = text_font.render(u'Next level', True, (255,255,255),(0,0,0))
    text_nextlevel_rect = text_nextlevel.get_rect()
    text_nextlevel_rect.center = (width/2,height/2+200)
    text_congratulation = text_font.render(u'Congratulation!', True, (255,255,255),(0,0,0))
    text_congratulation_rect = text_congratulation.get_rect()
    text_congratulation_rect.center = (width/2,height/2-200)

    text_font1 = pygame.font.SysFont("times new roman", 20)
    text_dfs = text_font1.render(u'View DFS searching', True, (255,255,255))
    text_dfs_rect = text_dfs.get_rect()
    text_dfs_rect.center = (width-130,100)
    text_bfs = text_font1.render(u'View BFS searching', True, (255,255,255))
    text_bfs_rect = text_bfs.get_rect()
    text_bfs_rect.center = (width-130,140)
    text_ucs = text_font1.render(u'View uniform cost searching', True, (255,255,255))
    text_ucs_rect = text_ucs.get_rect()
    text_ucs_rect.center = (width-130,180)
    text_As = text_font1.render(u'View Astar searching   ', True, (255,255,255))
    text_As_rect = text_As.get_rect()
    text_As_rect.center = (width-130,220)
    text_path = text_font1.render(u'View path   ', True, (255,255,255))
    text_path_rect = text_path.get_rect()
    text_path_rect.center = (width-130,260)
    text_skip = text_font1.render(u'Skip to Next Level', True, (255,255,255))
    text_skip_rect = text_skip.get_rect()
    text_skip_rect.center = (width-130,600)


    image_startmenu = pygame.image.load('images/background/startmenu.png')
    image_background = pygame.image.load('images/background/background.png')
    image_path = pygame.image.load("images/wall/path.png").convert_alpha()
    image_w = pygame.image.load("images/background/w.png").convert_alpha()
    image_asd = pygame.image.load("images/background/asd.png").convert_alpha()
    image_victory = pygame.image.load("images/background/victory.png").convert_alpha()


    text1 = pygame.image.load('images/background/startgame.png').convert()
    text1_rect = text1.get_rect()
    text1_rect.center = (width/2,height/2 + 100)
    
    maze_size = 2
    Maze = maze.createmaze(maze_size)
    while solution.solution_maze(Maze,'DFS') == False:
        Maze = maze.createmaze(maze_size)


    wall_location = []
    ice_location = []
    for i in range(2*maze_size+1):
        for j in range(2*maze_size+1):
            if Maze[i][j] == 0:
                wall_location.append((i,j))
            elif Maze[i][j] == 10:
                position_people = i*32,j*32
            elif Maze[i][j] == 1:
                position_treasure = i*32,j*32
            elif Maze[i][j] == 4:
                ice_location.append((i,j))

    me = people.People(position_people)

    walls = []
    ices = []
    for each in wall_location:
        position = each[0]*32,each[1]*32
        wa = wall.Wall(position, 0)
        walls.append(wa)

    for each in ice_location:
        position = each[0]*32,each[1]*32
        wa = wall.Wall(position, 1)
        ices.append(wa)
    
    treasure = pygame.image.load('images/wall/treasure.png')
    treasure_rect = treasure.get_rect()
    treasure_rect.left = position_treasure[0]
    treasure_rect.top = position_treasure[1]                                        
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if Gamestate == 0:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and text1_rect.collidepoint(event.pos):
                    Gamestate = 11
            screen.blit(image_startmenu,(0,0))
            screen.blit(text_startmenu,text_startmenu_rect)
            screen.blit(text1,text1_rect)

        if Gamestate == 11:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and text_dfs_rect.collidepoint(event.pos):
                    Gamestate = 12
                if event.button == 1 and text_bfs_rect.collidepoint(event.pos):
                    Gamestate = 13
                if event.button == 1 and text_As_rect.collidepoint(event.pos):
                    Gamestate = 14
                if event.button == 1 and text_ucs_rect.collidepoint(event.pos):
                    Gamestate = 15
                if event.button == 1 and text_path_rect.collidepoint(event.pos):
                    Gamestate = 16
                if event.button == 1 and text_skip_rect.collidepoint(event.pos):
                    Gamestate = 100


            
            key_pressed = pygame.key.get_pressed()
            if 1 not in key_pressed:
                key_state = 1;
            if key_pressed[K_w] and key_state == 1:
                me.moveUp()
                key_state = 0;
            if key_pressed[K_s] and key_state == 1:
                me.moveDown()
                key_state = 0;
            if key_pressed[K_a] and key_state == 1:
                me.moveLeft()
                key_state = 0;
            if key_pressed[K_d] and key_state == 1:
                me.moveRight()
                key_state = 0;

            location_temp = (int(me.rect.left/32),int(me.rect.top/32));
            if  Maze[location_temp[0]][location_temp[1]] == 0:
                if key_pressed[K_w]:
                    me.rect.top += me.speed
                if key_pressed[K_s]:
                    me.rect.top -= me.speed
                if key_pressed[K_a]:
                    me.rect.left += me.speed
                if key_pressed[K_d]:
                    me.rect.left -= me.speed
            elif Maze[location_temp[0]][location_temp[1]] == 1:
                Gamestate = 100

            screen.fill(bg)
            screen.blit(image_background,(0,0))
            screen.blit(treasure,treasure_rect)
            for each in walls:
                screen.blit(each.image1,each.rect)
            for each in ices:
                screen.blit(each.image1,each.rect)


            screen.blit(me.people,me.rect)
            screen.blit(text_dfs,text_dfs_rect)
            screen.blit(text_bfs,text_bfs_rect)
            screen.blit(text_As,text_As_rect)
            screen.blit(text_path,text_path_rect)
            screen.blit(text_ucs,text_ucs_rect)
            screen.blit(image_w,(width-167, height - 300))
            screen.blit(image_asd,(width-230, height - 230))
            screen.blit(text_skip,text_skip_rect)



        if Gamestate == 12:
            searching_process = solution.solution_maze(Maze,'DFS')
            visited = []
            for point in searching_process:
                visited.append([point[0],point[1]])
                screen.fill(bg)
                screen.blit(image_background,(0,0))
                screen.blit(treasure,treasure_rect)
                for each in walls:
                    screen.blit(each.image1,each.rect)
                for each in ices:
                    screen.blit(each.image1,each.rect)
                for path in visited:
                    screen.blit(image_path,(path[0]*32,path[1]*32))

                me.rect.left = 32 * point[0]
                me.rect.top = 32 * point[1]
                screen.blit(me.people,me.rect)
                pygame.display.flip()
                pygame.time.wait(200)

            me.rect.left = 32 * searching_process[0][0]
            me.rect.top = 32 * searching_process[0][1]
            Gamestate = 11

        if Gamestate == 13:
            searching_process = solution.solution_maze(Maze,'BFS')
            visited = []
            for point in searching_process:
                visited.append([point[0],point[1]])
                screen.fill(bg)
                screen.blit(image_background,(0,0))
                screen.blit(treasure,treasure_rect)
                for each in walls:
                    screen.blit(each.image1,each.rect)
                for each in ices:
                    screen.blit(each.image1,each.rect)
                for path in visited:
                    screen.blit(image_path,(path[0]*32,path[1]*32))
                me.rect.left = 32 * point[0]
                me.rect.top = 32 * point[1]
                screen.blit(me.people,me.rect)
                pygame.display.flip()
                pygame.time.wait(200)

            me.rect.left = 32 * searching_process[0][0]
            me.rect.top = 32 * searching_process[0][1]
            Gamestate = 11

        if Gamestate == 14:
            searching_process = solution.solution_maze(Maze,'A*')
            visited = []
            for point in searching_process:
                visited.append([point[0],point[1]])
                screen.fill(bg)
                screen.blit(image_background,(0,0))
                screen.blit(treasure,treasure_rect)
                for each in walls:
                    screen.blit(each.image1,each.rect)
                for each in ices:
                    screen.blit(each.image1,each.rect)
                for path in visited:
                    screen.blit(image_path,(path[0]*32,path[1]*32))
                me.rect.left = 32 * point[0]
                me.rect.top = 32 * point[1]
                screen.blit(me.people,me.rect)
                pygame.display.flip()
                pygame.time.wait(200)

            me.rect.left = 32 * searching_process[0][0]
            me.rect.top = 32 * searching_process[0][1]
            Gamestate = 11

        if Gamestate == 15:
            searching_process = solution.solution_maze(Maze,'uniform')
            visited = []
            for point in searching_process:
                visited.append([point[0],point[1]])
                screen.fill(bg)
                screen.blit(image_background,(0,0))
                screen.blit(treasure,treasure_rect)
                for each in walls:
                    screen.blit(each.image1,each.rect)
                for each in ices:
                    screen.blit(each.image1,each.rect)
                for path in visited:
                    screen.blit(image_path,(path[0]*32,path[1]*32))
                me.rect.left = 32 * point[0]
                me.rect.top = 32 * point[1]
                screen.blit(me.people,me.rect)
                pygame.display.flip()
                pygame.time.wait(200)

            me.rect.left = 32 * searching_process[0][0]
            me.rect.top = 32 * searching_process[0][1]
            Gamestate = 11


        if Gamestate == 16:
            searching_process = solution.solution_maze(Maze,'A*')
            path = solution.solution_to_path(searching_process)
            screen.blit(image_background,(0,0))
            for each in ices:
                screen.blit(each.image1,each.rect)
            for points in path:
                screen.blit(image_path,(points[0]*32,points[1]*32))           
            for each in walls:
                screen.blit(each.image1,each.rect)
            pygame.display.flip()
            pygame.time.wait(1000)


            Gamestate = 11



           

        if Gamestate == 100:
            screen.blit(image_victory,(0,0))
            screen.blit(text_nextlevel,text_nextlevel_rect)
            screen.blit(text_congratulation,text_congratulation_rect)
            pygame.display.flip()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and text_nextlevel_rect.collidepoint(event.pos):
                    Gamestate = 11

                    maze_size = min(maze_size + 1,10)
                    Maze = maze.createmaze(maze_size)
                    while solution.solution_maze(Maze,'DFS') == False:
                        Maze = maze.createmaze(maze_size)

                    wall_location = []
                    ice_location = []
                    for i in range(2*maze_size+1):
                        for j in range(2*maze_size+1):
                            if Maze[i][j] == 0:
                                wall_location.append((i,j))
                            elif Maze[i][j] == 10:
                                position_people = i*32,j*32
                            elif Maze[i][j] == 1:
                                position_treasure = i*32,j*32
                            elif Maze[i][j] == 4:
                                ice_location.append((i,j))

                    me = people.People(position_people)

                    walls = []
                    ices = []
                    for each in wall_location:
                        position = each[0]*32,each[1]*32
                        wa = wall.Wall(position,0)
                        walls.append(wa)

                    for each in ice_location:
                        position = each[0]*32,each[1]*32
                        wa = wall.Wall(position,1)
                        ices.append(wa)
                    
                    treasure = pygame.image.load('images/wall/treasure.png')
                    treasure_rect = treasure.get_rect()
                    treasure_rect.left = position_treasure[0]
                    treasure_rect.top = position_treasure[1]

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

