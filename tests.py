import unittest
from Maze import Maze
from GUI import Window
from Cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols,
        )

    def test_maze_create_cells_instance(self):
        num_cols = 10
        num_rows = 10
        screen_x = 1000
        screem_y = 600
        cell_sizeX = 800 // num_cols
        cell_sizeY = 600 // num_rows
        m1 = Maze(0, 0, num_rows, num_cols, cell_sizeX, cell_sizeY)
        # Check row count
        self.assertEqual(len(m1._Maze__cells), num_rows)

        # Check column count in every row
        for row in m1._Maze__cells:
            self.assertEqual(len(row), num_cols)

        # self.__cells is replace with m1._Maze__cells beacuse of name Mangling where variable with __ will be added with _ClassName
        # Check that all items are Cell instances
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertIsInstance(m1._Maze__cells[i][j], Cell)
        
    def test_maze_create_cells_with_win(self):
        num_cols = 10
        num_rows = 10
        screen_x = 1000
        screem_y = 600
        cell_sizeX = 800 // num_cols
        cell_sizeY = 600 // num_rows
        win = Window(screen_x,screem_y)
        m1 = Maze(0, 0, num_rows, num_cols, cell_sizeX, cell_sizeY,win)
        # Check row count
        self.assertEqual(len(m1._Maze__cells), num_rows)

        # Check column count in every row
        for row in m1._Maze__cells:
            self.assertEqual(len(row), num_cols)

        # self.__cells is replace with m1._Maze__cells beacuse of name Mangling where variable with __ will be added with _ClassName
        # Check that all items are Cell instances
        for i in range(num_rows):
            for j in range(num_cols):
                cell = m1._Maze__cells[i][j]
                self.assertIsInstance(cell, Cell)

                # 👇 Check that the correct Window is passed
                self.assertIs(cell._Cell__win, win)


    def test_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 10
        cell_size_x = 40
        cell_size_y = 40

        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        # Manually call the private method
        maze._Maze__break_entrance_and_exit()

        # Test entrance: top-left cell should have no top wall
        entrance_cell = maze._Maze__cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall)

        # Test exit: bottom-right cell should have no bottom wall
        exit_cell = maze._Maze__cells[num_rows - 1][num_cols - 1]
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_reset(self):
        num_rows = 3
        num_cols = 3
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        for row in m1._Maze__cells:
            for cell in row:
                cell.visited = True
        m1._Maze__reset_cells_visited()
        for row in m1._Maze__cells:
            for cell in row:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()

