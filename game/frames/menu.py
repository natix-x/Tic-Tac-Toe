from tkinter import Label, Button
from .modules.end_game_handler import EndGameHandler
from .modules.settings import Settings


class Menu:
    """
    creates updatable scoreboard, turn board, creates restart button and exit button
    """

    def __init__(self, localization, first_player=None, game_instance=None):
        self.localization = localization
        self.current_player = first_player
        self.game_instance = game_instance
        self.end_process = None
        self.winner_of_the_whole_game = None
        self.player_O_score = 0
        self.player_X_score = 0
        self.font = ("Arial", 13)
        self.scoreboard = Label(
            self.localization, background=Settings.background_color, width=10, height=8
        )
        self.scoreboard.place(x=30, y=120)
        self.player_X_score = 0
        self.player_O_score = 0
        self.turn_board_title = Label(
            self.localization, background=Settings.background_color, width=5, height=4
        )
        self.turn_board = Label(
            self.localization, background=Settings.background_color, width=5, height=4
        )
        self.turn_board.place(x=30, y=0)
        self.winner_of_the_whole_game = None
        self.end_process = None
        self.update_scoreboard()
        self.whose_turn(self.current_player)
        self.exit_button()

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
            font=self.font,
            fg=Settings.text_color,
        )
        self.who_is_the_winner()

    def who_is_the_winner(self):
        """
        displays who the winner of the whole game is
        :return: winner's nickname or None
        """
        if self.player_X_score != self.player_O_score:
            if self.player_X_score > self.player_O_score:
                self.winner_of_the_whole_game = self.game_instance.player_X_name
            else:
                self.winner_of_the_whole_game = self.game_instance.player_O_name
        else:
            self.winner_of_the_whole_game = None

        self.end_process = EndGameHandler(
            self.game_instance, winner=self.winner_of_the_whole_game
        )

    def whose_turn(self, current_player):
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
            fg=Settings.text_color,
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
            fg=Settings.text_color,
            font=self.font,
            command=lambda: board_instance.handle_restart("", board_instance.canvases),
        )
        restart_button.place(x=30, y=270)

    def exit_button(self):
        """
        creates button through which players can exit the game
        """
        end_button = Button(
            self.localization,
            text="Exit",
            height=3,
            width=10,
            command=lambda: self.end_process.end_game(),
            background=Settings.background_color,
            fg=Settings.text_color,
            font=self.font,
        )
        end_button.place(x=30, y=350)
