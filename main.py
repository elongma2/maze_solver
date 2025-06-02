from tkinter import Tk, BOTH, Canvas
from GUI import Window,Line,Point
from Cell import Cell
from Maze import Maze

if __name__ == '__main__':
    num_rows = 16
    num_cols = 10
    screen_x = 1000
    screem_y = 600
    cell_sizeX = 800 // num_cols
    cell_sizeY = 600 // num_rows
    win = Window(screen_x,screem_y)
    maze = Maze(0,0,num_rows,num_cols,cell_sizeX,cell_sizeY,win)
    win.wait_for_close()


    

