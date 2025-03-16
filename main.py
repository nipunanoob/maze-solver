from window import Window
from line import Line,Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(500, 400)
    p4 = Point(600, 500)

    # cell1 = Cell(win)
    # cell2 = Cell(win)
    # win.draw_cell(cell1, p1.x, p1.y, p2.x, p2.y)
    # win.draw_cell(cell2, p3.x, p3.y, p4.x, p4.y)

    # cell1.draw_move(cell2)
    # cell1.draw_move(win.get_canvas(),cell2,True)

    maze = Maze(220,75, 6, 5, 50, 50, win)
    if (maze.solve()):
        print("Maze solved!")
    else:
        print("Maze unsolved!")

    win.wait_for_close()

main()