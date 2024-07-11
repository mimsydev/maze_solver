from source.window import Window
from source.drawing import Line, Point
from source.maze import Maze

if __name__ == "__main__":
    print("starting the maze")
    win = Window(500,500)
    print("Built the window")
    maze = Maze(x1=0,y1=0,cell_size_x=10,cell_size_y=10,row_count=50,col_count=50,win=win)
    print(maze._cells)
    maze._draw_cells()
