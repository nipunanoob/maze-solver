from window import Window
from line import Line,Point
from cell import Cell

def main():
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(100, 150)
    p4 = Point(300, 200)
    p5 = Point(125,155)
    p6 = Point(175, 190)

    cell1 = Cell(True,True,False,False)
    cell2 = Cell()
    cell3 = Cell(False,True,False,False)
    cell4 = Cell()
    win.draw_cell(cell1, p1.x, p1.y, p2.x, p2.y)
    win.draw_cell(cell2, p3.x, p3.y, p2.x, p2.y)
    win.draw_cell(cell3, p3.x, p3.y, p4.x, p4.y)
    win.draw_cell(cell4, p5.x, p5.y, p6.x, p6.y)

    win.wait_for_close()

main()