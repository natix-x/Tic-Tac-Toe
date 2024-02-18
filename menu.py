from tkinter import Label


class Menu:
    def __init__(self, localization):
        self.localization = localization
        self.scoreboard = Label(self.localization, background="white")
        self.scoreboard.place(x=20, y=150)
        self.player_X_score = 0
        self.player_0_score = 0
        self.update_scoreboard()

    def update_scoreboard(self, winner=None):
        if winner == "X":
            self.player_X_score += 1
        elif winner == "O":
            self.player_0_score += 1

        self.scoreboard.config(text=f"Player X: {self.player_X_score}\nPlayer O: {self.player_0_score}")

    def whose_turn(self):
        pass



