from tkinter import Button, Canvas, messagebox
from game_logic import GameLogic
from drawing import Draw


class Board:
    def __init__(self, localization):
        self.localization = localization
        self.current_player = "X"
        self.buttons = [[" " for _ in range(3)] for _ in range(3)]
        self.canvases = [[None for _ in range(3)] for _ in range(3)]

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
        if self.buttons[row][col]["text"] == " ":
            self.canvases[row][col] = Canvas(
                self.localization,
                width=145,
                height=145,
                background="black",
                highlightthickness=0,
            )
            self.canvas = self.canvases[row][col]
            drawing = Draw(self.canvas)
            if self.current_player == "X":
                self.buttons[row][col].config(text=drawing.draw_X())
            else:
                self.buttons[row][col].config(text=drawing.draw_0())

            self.canvases[row][col].grid(row=row, column=col)

            game_logic = GameLogic(self.buttons)
            winning_combination = game_logic.check_if_win()
            if winning_combination:
                self.highlight_winning_combination(winning_combination)
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif game_logic.check_if_tie():
                messagebox.showinfo("Game Over", "Tie!")

            self.current_player = "O" if self.current_player == "X" else "X"

    def highlight_winning_combination(self, combination):
        if combination:
            for row, col in combination:
                self.canvases[row][col].config(bg="red")




