from tkinter import Canvas
from dataclasses import dataclass

@dataclass
class Point:
    x: int = 0
    y: int = 0

@dataclass
class Line:
    point_1: Point
    point_2: Point

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y,
                           fill=fill_color, width=2)
