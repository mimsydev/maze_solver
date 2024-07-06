from .window import Window
from .cell import Cell
from dataclasses import dataclass

class Maze:
    def __init__(self) -> None:
        self.x1: int
        self.y1: int
        self.row_count: int
        self.col_coint: int
        self.cell_size_x: int
        self.cell_size_y: int
        self.win: Window

    def _create_cells(self) -> None:
        raise NotImplementedError


