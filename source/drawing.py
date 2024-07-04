from tkinter import Canvas

class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
