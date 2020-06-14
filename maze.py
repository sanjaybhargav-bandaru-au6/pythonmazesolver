#!/bin/python3
import os
import sys
import argparse
import datetime


#    THIS FUNCTION SOLVES THE MAZE PROBLEM USING BACKTRACKING. IT   
#    RETURNS FALSE(-1) IF NO PATH IS AVAILABLE,OTHERWISE RETURNS TRUE.


def maze_Sol( x, y ):
    if maze[SIZE-1][SIZE-1] == 0:
        return False
    if (x==SIZE-1) and (y==SIZE-1):# if destination is reached
        solution[x][y] = 1;
        return True
    if (x>=0 and y>=0 and x<SIZE and y<SIZE #checking if we can visit in the cell or not 
        and solution[x][y] == 0 and maze[x][y] == 1):
        solution[x][y] = 1 # will be visiting the cell
        if maze_Sol(x+1, y): # will be going down
            return True
        if maze_Sol(x, y+1): # will be going right
            return True
        if maze_Sol(x-1, y): # will be going up
            return True
        if maze_Sol(x, y-1): # will be going left
            return True    
        solution[x][y] = 0; # will be backtracking
        return False;
    return False;


#    THIS FUNCTION PRINTS THE PATH.


def print_solution( sol ):
    f1.write("***\n" + "Following the path " + moveCheck(sol) + " leads to the destination:\n\n")
    for i in sol:
        for j in i:
            f1.write(" " + str(j) + " ")
        f1.write('\n') 
    now = datetime.datetime.now()
    f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S\n" + "***\n\n"))


# THIS FUNCTION RETURNS THE MOVEMENTS NEED TO BE MADE TO REACH THE DESTINATION.


def moveCheck( solved_maze ):
    n = len(solved_maze)
    reached = [[False for _ in range(n)] for _ in range(n)]
    arr = ""
    i = j = 0
    while i!=n-1 or  j!=n-1:
        if j == n-1:
            if solved_maze[i+1][j] == 1 and reached[i+1][j] == False:
                reached[i+1][j] = True
                i = i+1
                arr+="D"
            elif solved_maze[i][j-1] == 1 and reached[i][j-1] == False:
                reached[i][j-1] = True
                j = j-1
                arr+="L"  
        elif i == n-1:
            if solved_maze[i][j+1] == 1 and reached[i][j+1] == False:
                reached[i][j+1] = True
                j = j+1
                arr+="R"  
            elif solved_maze[i-1][j] == 1 and reached[i-1][j] == False:
                reached[i-1][j] = True
                i = i-1
                arr+="U"    
        else:
            if solved_maze[i+1][j] == 1 and reached[i+1][j] == False:
                reached[i+1][j] = True
                i = i+1
                arr+="D"
            elif solved_maze[i][j+1] == 1 and reached[i][j+1] == False:
                reached[i][j+1] = True
                j = j+1
                arr+="R"  
            elif solved_maze[i-1][j] == 1 and reached[i-1][j] == False:
                reached[i-1][j] = True
                i = i-1
                arr+="U"
            elif solved_maze[i][j-1] == 1 and reached[i][j-1] == False:
                reached[i][j-1] = True
                j = j-1
                arr+="L"
    return arr


#           DRIVER CODE

if __name__ == "__main__":	
    maze = []

    # ARGEPARSE FOR TAKING FILE ARGUMENTS FROM COMMAND LINE.
    parser = argparse.ArgumentParser()
    parser.add_argument("--s","--source",help="add source")
    parser.add_argument("--d","--destination",help="add destination")
    parser.add_argument("ipFile", help="Input File")
    parser.add_argument("opFile", help="Output File")
    args = parser.parse_args()
    f = open(args.ipFile,'r')# input file
    f1 = open(args.opFile,'a')# output file
    
    # GENERATING MAZE FROM THE INPUTS
    for data in f:
        [l.strip('\n\r') for l in data]
        maze.append([int(x) for x in data.split()])
    SIZE = len(maze)
    solution = [[0]*SIZE for _ in range(SIZE)]    

    # MAZE
    if(maze_Sol(0,0)):
        print_solution(solution)
    else:
        f1.write("***\n-1\n")
        f1.write("-1")
        now = datetime.datetime.now()
        f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S") + "\n***\n\n\n")