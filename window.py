from tkinter import Tk, BOTH, Canvas
from line import Line

class Window():
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Test title")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()

        self.__running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while (self.__running):
            self.redraw()
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell, x1, y1, x2, y2, fill_color="black"):
        cell.draw(self.__canvas, x1, y1, x2, y2, fill_color)
