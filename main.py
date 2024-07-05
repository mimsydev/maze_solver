from source.window import Window
from source.drawing import Line, Point

if __name__ == "__main__":
    win = Window(500,500)
    point_1 = Point(0,0)
    point_2 = Point(500,500)
    line=Line(point_1,point_2)
    win.draw_line(line, "red")
    win.wait_for_close()
