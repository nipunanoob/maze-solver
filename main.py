from window import Window
from line import Line,Point

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300,  200)
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p1)
    win.draw_line(line1, "black")
    win.draw_line(line2, "black")
    win.draw_line(line3, "black")
    win.wait_for_close()

main()