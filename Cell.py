from GUI import Window,Point,Line

class Cell:
    def __init__(self,window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, "black")

        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "black")
        
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, "black")
        
        # bottom wall using y2 instead as in GUI coordinates start from 0,0 top left and increases as it goes downwards
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "black")

    def draw_move(self,to_cell,undo=False):
        # find middle of current cell
        x_mid_self = (self.__x1 + self.__x2) // 2
        y_mid_self = (self.__y1 + self.__y2) // 2

        # find middle of next cell
        x_to_cell = (to_cell.__x1 + to_cell.__x2) // 2
        y_to_cell = (to_cell.__y1 + to_cell.__y2) // 2
        
        color = "grey" if undo else "red"

        move = Line(Point(x_mid_self,y_mid_self),Point(x_to_cell,y_to_cell))
        self.__win.draw_line(move,color)

        
        