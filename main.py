from tkinter import Tk, Frame
from board import Board
from menu import Menu
from settings import Settings
from title import Title
from start import Start


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
    title_frame.pack(fill="x")

    right_frame = Frame(
        root,
        bg=Settings.background_color,
        width=Settings.root_width * 0.25,
        height=Settings.root_height,
    )
    right_frame.pack(side="right", fill="y")
    board_frame = Frame(
        root,
        bg=Settings.background_color,
        width=Settings.root_width * 0.75,
        height=Settings.root_height * 0.8,
    )
    board_frame.pack(side="left", fill="both")

    Title(title_frame)
    start = Start(right_frame, board_frame)

    root.mainloop()


if __name__ == "__main__":
    tic_tac_toe()
