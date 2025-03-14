from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()
    
    def _create_cells(self):
        self._cells = [[Cell(self.win) for r in range(self.num_rows)] for c in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x_top_left= self.x1 + (i * self.cell_size_x)
        y_top_left= self.y1 + (j * self.cell_size_y)
        x_bot_right= x_top_left + self.cell_size_x
        y_bot_right = y_top_left + self.cell_size_y

        cell = self._cells[i][j]
        cell.draw(x_top_left, y_top_left, x_bot_right, y_bot_right)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

