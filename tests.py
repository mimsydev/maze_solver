import unittest
from source.maze import Maze

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.num_cols = 10
        self.num_rows = 14
        self.m1 = Maze(x1=0, y1=0, col_count=self.num_cols, row_count=self.num_rows,
                       cell_size_x=40, cell_size_y=20)

    def test_maze_rows(self) -> None:
        self.assertEqual(len(self.m1._cells), self.num_rows)

    def test_maze_cols(self) -> None:
        self.assertEqual(len(self.m1._cells[0]), self.num_cols)

    def test_maze_entex(self) -> None:
        self.assertTrue(not self.m1._cells[0][0].has_top_wall
                        and not self.m1._cells[-1][-1].has_bottom_wall)


if __name__ == "__main__":
    unittest.main()

