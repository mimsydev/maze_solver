from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, canvas_width: int, canvas_height: int) -> None:
        self.__root = Tk()
        self.__root.title("My Maze Solver")
        self.__canvas = Canvas(self.__root, width=canvas_width, height=canvas_height)
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # self.__root.mainloop()
        
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self) -> None:
        self.__is_running = False
