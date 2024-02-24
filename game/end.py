from tkinter import messagebox


class End:
    def __init__(self, start_instance, winner):
        self.start_instance = start_instance
        self.winner = winner

    def end_game(self):
        """
        asks if players really want to end current game. If yes displays winning message,
        asks if they want to start again and then restarts whole
        game. If no: closes game window
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
                self.start_instance.restart_game()
            else:
                self.start_instance.root.destroy()

    def winning_message(self):
        """
        displays final results according to scoreboard
        :return: message about final results
        """
        # Remove the condition for checking if the winner is None
        if self.winner is not None:
            win_message = messagebox.showinfo("Results", f"The winner is {self.winner}")
        else:
            tie_message = messagebox.showinfo("Results", "It's a tie!")
