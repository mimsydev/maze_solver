from .window import Window
from .cell import Cell
from dataclasses import dataclass
import time

@dataclass
class Maze:
    x1: int
    y1: int
    row_count: int
    col_count: int
    cell_size_x: int
    cell_size_y: int
    win: Window | None = None
    seed: int | None = None

    def __post_init__(self) -> None:
        self._create_cells()

    def solve(self) -> None:
        for i, row in enumerate(self._cells):
            for j, _ in enumerate(row):
                self._draw_cell(i,j)
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        self._cells = [[ Cell(self.x1+(j*self.cell_size_x),
                     self.y1+(i*self.cell_size_y),
                     self.x1+((j+1)*self.cell_size_x),
                     self.y1+((i+1)*self.cell_size_y),
                     self.win) for j in range(self.col_count) ] for i in range(self.row_count)]

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1,-1)

    def _break_walls(self) -> None:
        visited: list[tuple[int, int]] = []
        self._break_walls_r(visited, 0, 0)

    def _break_walls_r(self, visited: list[tuple[int,int]], i: int, j:int) -> None:
        visited.append((i,j))


    def _draw_cell(self, i: int = 0, j: int = 0) -> None:
        self._cells[i][j].draw()
        self._animate()

    def _animate(self) -> None:
        self.win.redraw()
        time.sleep(0.01)
