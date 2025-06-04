
from Cell import Cell
from time import sleep
import random
import time
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,

        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self.__cells = []
        if self.seed is not None:
            random.seed(self.seed)
        #start the maze
        self.create_cells()
        time.sleep(10)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

        

    def create_cells(self):
        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):
                cell = Cell(self.win)
                row_cells.append(cell)
            self.__cells.append(row_cells)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__draw_cells(i,j)

    def __draw_cells(self,i,j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = self.__cells[i][j]
        cell.draw(x1, y1, x2, y2)
        if self.win is not None:
            self.__animate()

    def __animate(self):
        self.win.redraw()
        sleep(0.05)
        
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cells(0,0)
        self.__cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self.__draw_cells(self.num_rows - 1,self.num_cols - 1)

    def __break_walls_r(self,i,j):
        #i is the row and j is the col
        #dfs implementation. dont necessarily have to go down can be in different directions as long as we reach to thge max depth possible

        current_cell = self.__cells[i][j]
        current_cell.visited = True
        while True:
            directions = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                directions.append(("up", i - 1, j))
            if i < self.num_rows - 1 and not self.__cells[i + 1][j].visited:
                directions.append(("down", i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                directions.append(("left", i, j - 1))
            if j < self.num_cols - 1 and not self.__cells[i][j + 1].visited:
                directions.append(("right", i, j + 1))

            if not directions:
                self.__draw_cells(i,j)
                return
            else:
                direction, next_i, next_j = random.choice(directions)
                next_cell = self.__cells[next_i][next_j]
                if direction == "up":
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                elif direction == "down":
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                elif direction == "left":
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                elif direction == "right":
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False

                self.__break_walls_r(next_i, next_j)
    def __reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,row,col):
        self.__animate()
        self.__cells[row][col].visited = True
        if self.__cells[self.num_rows-1][self.num_cols-1].visited:
            return True
        
        #up direction
        if row > 0 and not self.__cells[row - 1][col].visited and not self.__cells[row][col].has_top_wall:
            self.__cells[row][col].draw_move(self.__cells[row - 1][col])
            if self._solve_r(row-1,col): 
                return True
            else:
                self.__cells[row-1][col].draw_move(self.__cells[row][col],undo=True)

        #down direction
        if row < self.num_rows - 1 and not self.__cells[row + 1][col].visited and not self.__cells[row][col].has_bottom_wall:
            self.__cells[row][col].draw_move(self.__cells[row + 1][col])
            if self._solve_r(row+1,col): 
                return True
            else:
                self.__cells[row+1][col].draw_move(self.__cells[row][col],undo=True)
        
        #left direction
        if col > 0 and not self.__cells[row][col - 1].visited and not self.__cells[row][col].has_left_wall:
            self.__cells[row][col].draw_move(self.__cells[row][col - 1])
            if self._solve_r(row,col-1): 
                return True
            else:
                self.__cells[row][col-1].draw_move(self.__cells[row][col],undo=True)

        #right direction
        if col < self.num_cols - 1 and not self.__cells[row][col + 1].visited and not self.__cells[row][col].has_right_wall:
            self.__cells[row][col].draw_move(self.__cells[row][col + 1])
            if self._solve_r(row,col+1): 
                return True
            else:
                self.__cells[row][col+1].draw_move(self.__cells[row][col],undo=True)
        return False

        
                    


                

            

