from GUI import Window,Point,Line

class Cell:
    def __init__(self,window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win is None:
            return  # skip drawing if no window

        # Left wall
        line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        color = "black" if self.has_left_wall else "#d9d9d9"
        self.__win.draw_line(line, color)

        # Right wall
        line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        color = "black" if self.has_right_wall else "#d9d9d9"
        self.__win.draw_line(line, color)

        # Top wall
        line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        color = "black" if self.has_top_wall else "#d9d9d9"
        self.__win.draw_line(line, color)

        # Bottom wall
        line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        color = "black" if self.has_bottom_wall else "#d9d9d9"
        self.__win.draw_line(line, color)


    def draw_move(self,to_cell,undo=False):
        # find middle of current cell
        x_mid_self = (self.__x1 + self.__x2) // 2
        y_mid_self = (self.__y1 + self.__y2) // 2

        # find middle of next cell
        x_to_cell = (to_cell.__x1 + to_cell.__x2) // 2
        y_to_cell = (to_cell.__y1 + to_cell.__y2) // 2
        
        color = "grey" if undo else "red"

        move = Line(Point(x_mid_self,y_mid_self),Point(x_to_cell,y_to_cell))
        if self.__win is not None:
            self.__win.draw_line(move,color)
    
    


        
        