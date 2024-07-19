from source.window import Window
from source.drawing import Line, Point
from source.maze import Maze

if __name__ == "__main__":
    print("starting the maze")
    win = Window(502,502)
    print("Built the window")
    maze = Maze(x1=1,y1=1,cell_size_x=20,cell_size_y=20,row_count=25,col_count=25,win=win)
    maze.draw_maze()
    maze.solve_maze()
    if maze.win:
        maze.win.wait_for_close()
    else:
        raise ValueError("Win is not defined")
