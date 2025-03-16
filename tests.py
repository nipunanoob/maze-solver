import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_single_row(self):
        num_cols = 5
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_zero_row(self):
        num_cols = 5
        num_rows = 0
        with self.assertRaises(ValueError) as cm:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(cm.exception.args[0],"Number of rows and column must be greater than zero for creating Maze")

    def test_maze_create_cells_zero_column(self):
        num_cols = 0
        num_rows = 10
        with self.assertRaises(ValueError) as cm:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(cm.exception.args[0],"Number of rows and column must be greater than zero for creating Maze")

    def test_maze_create_cells_negative_column(self):
        num_cols = -5
        num_rows = 10
        with self.assertRaises(ValueError) as cm:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(cm.exception.args[0],"Number of rows and column must be greater than zero for creating Maze")

    def test_maze_create_cells_negative_row(self):
        num_cols = 5
        num_rows = -7
        with self.assertRaises(ValueError) as cm:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(cm.exception.args[0],"Number of rows and column must be greater than zero for creating Maze")
    
    def test_maze_create_cells_large(self):
        num_cols = 1000
        num_rows = 1000
        with self.assertRaises(ValueError) as cm:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(cm.exception.args[0],"Maze dimensions cannot exceed 100x100")

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 25
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        top_left_cell = maze._cells[0][0]
        bottom_right_cell = maze._cells[maze.num_cols - 1][maze.num_rows - 1]

        self.assertFalse(top_left_cell.has_top_wall) 
        self.assertFalse(bottom_right_cell.has_down_wall) 

    
    def test_reset_cells_visited(self):

        num_cols = 25
        num_rows = 25
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        cells = maze._cells
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(cells[i][j]._visited)

if __name__ == "__main__":
    unittest.main()