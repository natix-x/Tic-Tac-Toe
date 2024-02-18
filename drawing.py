from tkinter import Canvas


class Draw:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw_X(self):
        self.canvas.create_line(20, 20, 120, 120, width=15, fill="white")
        self.canvas.create_line(20, 120, 120, 20, width=15, fill="white")
        return "X"

    def draw_0(self):
        self.canvas.create_oval(20, 20, 120, 120, width=15, outline="white")
        return "0"

    @staticmethod
    def highlight_winning_combination(combination, canvases):
        if combination:
            for row, col in combination:
                canvases[row][col].config(bg="red")


