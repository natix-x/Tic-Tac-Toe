from tkinter import Button, Canvas, messagebox
from game_logic import GameLogic
from drawing import Draw


class Board:
    def __init__(self, localization):
        self.localization = localization
        self.current_player = "X"
        self.buttons = [[" " for _ in range(3)] for _ in range(3)]
        self.canvas = Canvas(self.localization, width=100, height=100, background="black",highlightthickness=0)
        self.drawing = Draw(self.canvas)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(
                    localization,
                    text=" ",
                    height=10,
                    width=20,
                    command=lambda row=i, col=j: self.make_move(row, col),
                    background="black",
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        self.row = row
        self.col = col
        if self.buttons[row][col]["text"] == " ":
            canvas = Canvas(self.localization, width=100, height=100, background="black", highlightthickness=0)
            self.canvas = canvas
            drawing = Draw(self.canvas)
            if self.current_player == "X":
                self.buttons[row][col].config(text=drawing.draw_X())
            else:
                self.buttons[row][col].config(text=drawing.draw_0())
            canvas.grid(row=row, column=col)

            if self.check_if_win():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.check_if_tie():
                messagebox.showinfo("Game Over", "TIE!")

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_if_win(self):
        game_logic = GameLogic(self.buttons)
        return game_logic.check_if_win()

    def check_if_tie(self):
        game_logic = GameLogic(self.buttons)
        return game_logic.check_if_tie()