
from Cell import Cell
from time import sleep

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.create_cells()

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
        self.__animate()

    def __animate(self):
        self.win.redraw()
        sleep(0.05)

