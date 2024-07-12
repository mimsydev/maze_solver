from __future__ import annotations
from dataclasses import dataclass
from .drawing import Line, Point
from .window import Window

@dataclass
class Cell:
    _x1: int
    _y1: int
    _x2: int
    _y2: int
    _win: Window | None = None
    has_top_wall: bool = True
    has_right_wall: bool = True
    has_bottom_wall: bool = True
    has_left_wall: bool = True

    def draw(self) -> None:
        tl_point = Point(self._x1,self._y1)
        tr_point = Point(self._x2,self._y1)
        br_point = Point(self._x2,self._y2)
        bl_point = Point(self._x1,self._y2)

        top_wall = Line(tl_point,tr_point)
        right_wall = Line(tr_point,br_point)
        bottom_wall = Line(br_point,bl_point)
        left_wall = Line(bl_point,tl_point)
        self._win.draw_line(top_wall, "black" if self.has_top_wall else "#d9d9d9")
        self._win.draw_line(right_wall, "black" if self.has_right_wall else "#d9d9d9")
        self._win.draw_line(bottom_wall, "black" if self.has_bottom_wall else "#d9d9d9")
        self._win.draw_line(left_wall, "black" if self.has_left_wall else "#d9d9d9")

    def draw_move(self, to_cell: Cell, undo: bool = False) -> None:
        s_point = Point((self._x1+self._x2)//2, (self._y1+self._y2)//2)
        e_point = Point((to_cell._x1+to_cell._x2)//2, (to_cell._y1+to_cell._y2)//2)
        move_line = Line(s_point,e_point)
        self._win.draw_line(move_line, "gray" if undo else "red")
