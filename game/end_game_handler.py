from tkinter import messagebox


class EndGameHandler:
    """
    handler of exit game button
    """

    def __init__(self, game_instance, winner):
        self.game_instance = game_instance
        self.winner = winner

    def end_game(self):
        """
        asks if players really want to end current game. If yes displays winning message,
        asks if they want to start again and then restarts whole
        game. If no: closes game window
        :return: three messageboxes
        """
        end = messagebox.askyesno(
            "Game Over",
            "Do you really want to end this game?",
            icon="question",
            default="no",
        )
        if end:
            self.winning_message()
            again = messagebox.askyesno(
                "Game Over",
                "Do you want to start another game?",
                icon="question",
                default="yes",
            )
            if again:
                self.game_instance.window_instance.restart_game()
            else:
                self.game_instance.window_instance.end_game()

    def winning_message(self):
        """
        displays final results according to scoreboard
        :return: message about final results
        """
        if self.winner is not None:
            win_message = messagebox.showinfo("Results", f"The winner is {self.winner}")
        else:
            tie_message = messagebox.showinfo("Results", "It's a tie!")
