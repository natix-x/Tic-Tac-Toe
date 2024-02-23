from tkinter import messagebox


class End:
    def __init__(self, start_instance):
        self.start_instance = start_instance

    def end_game(self):
        """
        asks if players really want to end current game. If yes asks do they want to start again and then restarts whole
        game. If no: closes game window
        """
        end = messagebox.askyesno(
            "Game Over",
            "Do you want to end this game?",
            icon="question",
            default="no",
        )
        if end:
            again = messagebox.askyesno(
                "Game Over",
                "Do you want to play again?",
                icon="question",
                default="yes",
            )
            if again:
                self.start_instance.restart_game()
            else:
                self.start_instance.root.destroy()
