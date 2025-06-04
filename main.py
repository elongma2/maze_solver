from GUI import Window
from Maze import Maze
import sys
if __name__ == '__main__':
    num_rows = 5
    num_cols = 5
    screen_x = 1000
    screem_y = 600
    cell_sizeX = 800 // num_cols
    cell_sizeY = 600 // num_rows
    
    sys.setrecursionlimit(10000)
    win = Window(screen_x,screem_y)

    maze = Maze(0,0,num_rows,num_cols,cell_sizeX,cell_sizeY,win,10)
    print("Maze Created")

    is_solved = maze.solve()
    if is_solved:
        print("Maze Solved")
    else:
        print("Maze Not Solved")

    win.wait_for_close()


    

