from tkinter import Label, Button
from settings import Settings


class Menu:
    def __init__(self, localization):
        self.localization = localization
        self.text_color = "white"
        self.scoreboard = Label(
            self.localization, background=Settings.background_color, width=10, height=8
        )
        self.scoreboard.place(x=30, y=120)
        self.player_X_score = 0
        self.player_O_score = 0
        self.turn_board_title = Label(
            self.localization,
            background=Settings.background_color,
            width=5,
            height=4)
        self.turn_board = Label(
            self.localization, background=Settings.background_color, width=5, height=4
        )
        self.turn_board.place(x=30, y=0)
        self.current_player = "X"
        self.update_scoreboard()
        self.whose_turn()
        self.end_button()

    def update_scoreboard(self, winner=None):
        """
        updates scoreboard: adds one point to the winner's (X or 0) scoreboard
        :param winner: player who won the round
        :return: updated scoreboard
        """
        if winner == "X":
            self.player_X_score += 1
        elif winner == "O":
            self.player_O_score += 1

        self.scoreboard.config(
            text=f"Scoreboard:\nPlayer X: {self.player_X_score}\nPlayer O: {self.player_O_score}",
            font=("Arial", 13),
            fg=self.text_color,
        )

    def whose_turn(self, current_player=None):
        """
        displays whose turn is now
        :param current_player: player whose turn is now
        :return: update turn_board
        """
        if current_player == "O":
            self.current_player = "O"
        else:
            self.current_player = "X"

        self.turn_board.config(
            text=f"Turn:\n\n{self.current_player}",
            font=("Arial", 20),
            fg=self.text_color,
        )

    def restart_button(self, board_instance):
        """
        while clicked displays the message if players surely want to restart the game;
        if yes: restarts board
        if no: players can continue their game if game is not won by any of them
        :param board_instance: current board
        :return: updated board
        """
        restart_button = Button(
            self.localization,
            text="Restart",
            height=3,
            width=10,
            background=Settings.background_color,
            fg=self.text_color,
            font=("Arial", 13),
            command=lambda: board_instance.handle_restart("", board_instance.canvases)
        )
        restart_button.place(x=30, y=270)

    def end_button(self):
        end_button = Button(
            self.localization,
            text="New game",
            height=3,
            width=10,
            command = self.end_game(),
            background=Settings.background_color,
            fg = self.text_color,
            font = ("Arial", 13)
        )
        end_button.place(x=30, y=350)

    def end_game(self):
        pass

