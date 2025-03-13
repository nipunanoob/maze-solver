from window import Window
from line import Line,Point
from cell import Cell

def main():
    win = Window(800, 600)

    p1 = Point(51, 100)
    p2 = Point(150, 200)
    p3 = Point(200, 150)
    p4 = Point(300, 200)

    cell1 = Cell()
    cell2 = Cell()
    win.draw_cell(cell1, p1.x, p1.y, p2.x, p2.y)
    win.draw_cell(cell2, p3.x, p3.y, p4.x, p4.y)

    cell1.draw_move(win.get_canvas(),cell2)
    cell1.draw_move(win.get_canvas(),cell2,True)

    win.wait_for_close()

main()