from tkinter import Label
from settings import Settings


class Title:
    def __init__(
        self, localization, player_X_name=None, player_O_name=None, chosen_player=None
    ):
        self.localization = localization
        self.player_X_name = player_X_name
        self.player_O_name = player_O_name
        self.chosen_player = chosen_player
        self.title_board = Label(
            self.localization,
            background=Settings.background_color,
            text="Tic Tac Toe",
            fg=Settings.text_color,
            font=("Arial", 45),
        )
        self.title_board.place(relx=0.4, rely=0.5, anchor="center")
        self.player_board = None

    def player_board_update(self):
        """
        assigns X and O symbols to players' nicknames
        """
        self.player_board = Label(
            self.localization, background=Settings.background_color
        )
        self.player_board.place(relx=0.9, rely=0.4, anchor="center")

        text = f"X: {self.player_X_name}\nO: {self.player_O_name}"
        self.player_board.config(text=text, fg=Settings.text_color, font=("Arial", 15))
