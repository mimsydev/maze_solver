from .window import Window
from .cell import Cell
from dataclasses import dataclass

@dataclass
class Maze:
    x1: int
    y1: int
    row_count: int
    col_count: int
    cell_size_x: int
    cell_size_y: int
    win: Window
    _cells: list[list[Cell]]

    def __post_init__(self) -> None:
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = [[ Cell(x1+(j*self.cell_size_x),
                     y1+(j*self.cell_size_y),
                     x1+((j+1)*self.cell_size_x),
                     y1+((j+1)*self.cell_size_y),
                     self.win) for j in range(col_count) ] for i in range(row_count)]
