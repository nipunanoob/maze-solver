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
            win=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        

        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        MAX_ROWS = 100
        MAX_COLS = 100
        if self.num_rows <= 0 or self.num_cols <= 0:
            raise ValueError("Number of rows and column must be greater than zero for creating Maze")
        elif self.num_rows >= MAX_COLS or self.num_cols >= MAX_COLS:
            raise ValueError(f"Maze dimensions cannot exceed {MAX_ROWS}x{MAX_COLS}")
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
        if self.win != None:
            cell.draw(x_top_left, y_top_left, x_bot_right, y_bot_right)
            self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        max_row_idx = self.num_rows - 1
        max_col_idx = self.num_cols - 1
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[max_col_idx][max_row_idx]
        top_left_cell.has_top_wall = False
        self._draw_cell(0,0)
        bottom_right_cell.has_down_wall = False
        self._draw_cell(max_col_idx, max_row_idx)
