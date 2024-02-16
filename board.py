from tkinter import Button, Canvas, messagebox


class Board:
    def __init__(self, localization):
        self.localization = localization
        self.current_player = "X"
        self.buttons = [[" " for _ in range(3)] for _ in range(3)]

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
        self.row = row
        self.col = col
        if self.buttons[row][col]["text"] == " ":
            canvas = Canvas(self.localization, width=100, height=100)
            self.canvas = canvas
            if self.current_player == "X":
                self.buttons[row][col].config(text=self.draw_X())
            else:
                self.buttons[row][col].config(text=self.draw_0())
            canvas.grid(row=row, column=col)

            if self.check_if_win():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.check_if_tie():
                messagebox.showinfo("Game Over", "TIE!")

            self.current_player = "O" if self.current_player == "X" else "X"

    def draw_X(self):
        self.canvas.create_line(0, 0, 95, 95, width=15)
        self.canvas.create_line(0, 95, 95, 0, width=15)
        return "X"

    def draw_0(self):
        self.canvas.create_oval(10, 10, 95, 95, width=15)
        return "0"

    def check_if_win(self):
        for i in range(3):
            if (
                self.buttons[i][0]["text"] != " "
                and self.buttons[i][0]["text"]
                == self.buttons[i][1]["text"]
                == self.buttons[i][2]["text"]
            ):
                return True
            elif (
                self.buttons[0][i]["text"] != " "
                and self.buttons[0][i]["text"]
                == self.buttons[1][i]["text"]
                == self.buttons[2][i]["text"]
            ):
                return True
        if (
            self.buttons[0][2]["text"] != " "
            and self.buttons[0][2]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][0]["text"]
        ):
            return True
        elif (
            self.buttons[0][0]["text"] != " "
            and self.buttons[0][0]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][2]["text"]
        ):
            return True

    def check_if_tie(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                        return False
        return True
