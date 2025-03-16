from line import Point, Line
from tkinter import Tk, BOTH, Canvas
from window import Window

class Cell():

    def __init__(self, win: Window = None, has_left_wall=True, has_top_wall=True, has_right_wall=True, has_down_wall=True):

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_down_wall = has_down_wall

        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0

        self.win=win
        self._visited = False        
    
    def draw(self, x1, y1, x2, y2, fill_color="black"):

        if (x2 <= x1 or y2 <= y1):
            raise Exception("Draw() accepts (x,y) of top left and bottom right respectively")

        self._x1 = x1 #Leftmost
        self._y1 = y1 #Topmost
        self._x2 = x2 #Rightmost
        self._y2 = y2 #Botmost

        p1 = Point(x1,y1)
        p2 = Point(x2,y1)
        p3 = Point(x2,y2)
        p4 = Point(x1,y2) 

        l1 = Line(p1, p4) #Left
        l2 = Line(p1, p2) #Top
        l3 = Line(p2, p3) #Right
        l4 = Line(p3, p4) #Bot

        if self.has_left_wall:
            l1.draw(self.win.get_canvas(), fill_color)
        else:
            l1.draw(self.win.get_canvas(), "#d9d9d9")

        if self.has_top_wall:
            l2.draw(self.win.get_canvas(), fill_color)
        else:
            l2.draw(self.win.get_canvas(), "#d9d9d9")
            
        if self.has_right_wall:
            l3.draw(self.win.get_canvas(), fill_color)
        else:
            l3.draw(self.win.get_canvas(), "#d9d9d9")

        if self.has_down_wall:
            l4.draw(self.win.get_canvas(), fill_color)
        else:
            l4.draw(self.win.get_canvas(), "#d9d9d9")
            
    def draw_move(self, to_cell: "Cell", undo=False):
        first_cell_center = Point(
            (self._x1 + self._x2) // 2,  # Calculate x-coordinate center
            (self._y1 + self._y2) // 2   # Calculate y-coordinate center
        )
        second_cell_center = Point(
            (to_cell._x1 + to_cell._x2) // 2,
            (to_cell._y1 + to_cell._y2) // 2
        )

        line = Line(first_cell_center, second_cell_center)
        if undo:
            line.draw(self.win.get_canvas(), "gray")
        else:
            line.draw(self.win.get_canvas(), "red")
