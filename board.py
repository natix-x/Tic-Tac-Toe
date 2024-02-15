from tkinter import Button


class Board:
    def __init__(self, localization):
        self.localization = localization
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(
                    localization,
                    text=" ",
                    height=10,
                    width=20,
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col].config(text=self.current_player)

            self.current_player = "O" if self.current_player == "X" else "X"

    def draw_X(self):
        pass

    def draw_0(self):
        pass


    def check_if_win(self):
        pass

    def check_if_tie(self):
        pass
