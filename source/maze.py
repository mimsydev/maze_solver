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
    win: Window

    def __post_init__(self) -> None:
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = [[ Cell(self.x1+(j*self.cell_size_x),
                     self.y1+(j*self.cell_size_y),
                     self.x1+((j+1)*self.cell_size_x),
                     self.y1+((j+1)*self.cell_size_y),
                     self.win) for j in range(self.col_count) ] for i in range(self.row_count)]

    def _draw_cells(self, i: int = 0, j: int = 0) -> None:
        for row in self._cells:
            print(row)
            for cell in row:
                cell.draw()
                self._animate()


    def _animate(self) -> None:
        while True:
            self.win.redraw()
            time.sleep(0.05)
