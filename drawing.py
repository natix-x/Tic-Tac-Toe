from tkinter import Canvas


from tkinter import Canvas

class Draw:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw_X(self):
        self.canvas.create_line(10, 10, 90, 90, width=15, fill="white")
        self.canvas.create_line(10, 90, 90, 10, width=15, fill="white")
        return "X"

    def draw_0(self):
        self.canvas.create_oval(10, 10, 90, 90, width=15, outline="white")
        return "0"

    #def draw_win_line(self, row=None, col=None, diagonal=None):
    #    x1, y1, x2, y2 = self.calculate_coordinates(row, col, diagonal)
    #    canva = Canvas(
    #        self.localization,
    #        width=300,
    #        height=300,
    #        background="black",
    #        highlightthickness=0,
    #    )
    #    canva.create_line(x1=x1, y1=y1, x2=x2, y2=y2, width=5, fill="red")
    #    canva.grid(row=row, column=col)

    #def calculate_coordinates(self, row=None, col=None, diagonal=None):
    #    if diagonal == "left_to_right_up":
    #        return 10, 290, 290, 10
    #    elif diagonal == "left_to_right_down":
    #        return 10, 10, 290, 290



