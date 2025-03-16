from cell import Cell
import time
import random

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
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win 

        random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        print("Breaking walls")
        self._break_walls_r(0,0)
        print("Walls broken, maze created :D")
    
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
        print(f"Destroying wall at entrance (0,0)")
        self._draw_cell(0,0)
        bottom_right_cell.has_down_wall = False
        print(f"Destroying wall at exit ({max_col_idx},{max_row_idx})")
        self._draw_cell(max_col_idx, max_row_idx)

    def _break_walls_r(self, i , j):
        current_idx = (i, j)
        self._cells[i][j]._visited = True #i is col idx, j is row idx
        while True:
            non_visited_neighbours = []
            if i > 0 and  not self._cells[i-1][j]._visited: #check left neighbour
                    non_visited_neighbours.append((i-1, j))
            if i < self.num_cols - 1 and not self._cells[i+1][j]._visited: #check right neighbour
                    non_visited_neighbours.append((i+1, j))
            if j > 0 and  not self._cells[i][j-1]._visited: #check top neighbour
                    non_visited_neighbours.append((i, j-1))
            if j < self.num_rows - 1 and not self._cells[i][j+1]._visited: #check bot neighbour
                    non_visited_neighbours.append((i, j+1))
            if len(non_visited_neighbours) == 0:
                self._draw_cell(i, j)
                return
        
            next_cell_idx = non_visited_neighbours[random.randrange(0,len(non_visited_neighbours))]
            direction = tuple(x - y for x, y in zip(next_cell_idx, current_idx))
            if direction == (1,0):
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i+1,j)
            elif direction == (-1,0):
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i-1,j)
            elif direction == (0, 1):
                self._cells[i][j].has_down_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i,j+1)
            elif direction == (0, -1):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_down_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i,j-1)

            self._break_walls_r(next_cell_idx[0],next_cell_idx[1])