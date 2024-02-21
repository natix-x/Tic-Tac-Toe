from tkinter import Label


class Title:
    def __init__(self, localization):
        self.localization = localization
        self.title_board = Label(
            self.localization, background="black", text="Tic Tac Toe", fg="white",
            font=("Arial", 45)
        )
        self.title_board.place(relx=0.5, rely=0.5, anchor='center')

