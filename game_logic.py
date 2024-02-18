from tkinter import messagebox


class GameLogic:
    def __init__(self, buttons):
        self.buttons = buttons

    def check_if_win(self):
        for i in range(3):
            if (
                self.buttons[i][0]["text"] != " "
                and self.buttons[i][0]["text"]
                == self.buttons[i][1]["text"]
                == self.buttons[i][2]["text"]
            ):
                return [(i, 0), (i, 1), (i, 2)]
            elif (
                self.buttons[0][i]["text"] != " "
                and self.buttons[0][i]["text"]
                == self.buttons[1][i]["text"]
                == self.buttons[2][i]["text"]
            ):
                return [(0, i), (1, i), (2, i)]
        if (
            self.buttons[0][0]["text"] != " "
            and self.buttons[0][0]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][2]["text"]
        ):
            return [(0, 0), (1, 1), (2, 2)]
        elif (
            self.buttons[0][2]["text"] != " "
            and self.buttons[0][2]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][0]["text"]
        ):
            return [(0, 2), (1, 1), (2, 0)]
        return None

    def check_if_tie(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                    return False
        return True

    def restart_board(self, canvases):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
                if canvases[i][j] is not None:
                    canvases[i][j].destroy()

    def handle_restart(self, message, canvases):
        restart = messagebox.askyesno("Game Over", f"{message} Do you want to restart?", icon='question',default='yes')
        if restart:
            self.restart_board(canvases)