from line import Point, Line
from tkinter import Tk, BOTH, Canvas

class Cell():

    def __init__(self, has_left_wall=True, has_top_wall=True, has_right_wall=True, has_down_wall=True):

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_down_wall = has_down_wall

        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
    
    def draw(self, canvas:Canvas, x1, y1, x2, y2, fill_color):

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
            l1.draw(canvas, fill_color)
            
        if self.has_top_wall:
            l2.draw(canvas, fill_color)
            
        if self.has_right_wall:
            l3.draw(canvas, fill_color)
            
        if self.has_down_wall:
            l4.draw(canvas, fill_color)
            

