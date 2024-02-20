from tkinter import *
from board import Board
from menu import Menu
from settings import Settings


def tic_tac_toe():
    root = Tk()

    root.configure(bg=Settings.background_color)
    root.geometry(f"{Settings.root_width}x{Settings.root_height}")
    root.title("Tic Tac Toe")
    root.resizable(False, False)

    title_frame = Frame(
        root,
        bg=Settings.background_color,
        width=Settings.root_width * 0.75,
        height=Settings.root_height * 0.2,
    )
    title_frame.place(x=0, y=0)

    right_frame = Frame(
        root,
        bg=Settings.background_color,
        width=Settings.root_width * 0.25,
        height=Settings.root_height,
    )
    right_frame.place(x=Settings.root_width * 0.75, y=Settings.root_height * 0.2)

    board_frame = Frame(
        root,
        bg=Settings.background_color,
        width=Settings.root_width * 0.75,
        height=Settings.root_height * 0.8,
    )
    board_frame.place(x=0, y=Settings.root_height * 0.2)

    right_menu = Menu(right_frame)
    board = Board(board_frame, right_menu)

    root.mainloop()


if __name__ == "__main__":
    tic_tac_toe()
