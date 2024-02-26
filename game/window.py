from settings import Settings
from tkinter import Tk, Frame
from game_init import GameInit


class Window:
    def __init__(self):
        self.root = Tk()
        self.board_frame = None
        self.menu_frame = None
        self.title_frame = None
        self.frames_init()
        self.tic_tac_toe()

    def frames_init(self):
        """
        initialize frame creation
        :return: title frame, board game, right frame
        """
        self.root.configure(bg=Settings.background_color)
        self.root.geometry(f"{Settings.root_width}x{Settings.root_height}")
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        self.title_frame = Frame(
            self.root,
            bg=Settings.background_color,
            width=Settings.root_width * 0.75,
            height=Settings.root_height * 0.2,
        )
        self.title_frame.pack(fill="x")

        self.menu_frame = Frame(
            self.root,
            bg=Settings.background_color,
            width=Settings.root_width * 0.25,
            height=Settings.root_height,
        )
        self.menu_frame.pack(side="right", fill="y")
        self.board_frame = Frame(
            self.root,
            bg=Settings.background_color,
            width=Settings.root_width * 0.75,
            height=Settings.root_height * 0.8,
        )
        self.board_frame.pack(side="left", fill="both")

    def tic_tac_toe(self):
        """
        creates window with tic-tac-toe game presence initiation
        :return: tic-tac-toe game window
        """
        game_init = GameInit(self)
        self.root.mainloop()

    def restart_game(self):
        """
        destroys current window and creates a new one
        :return: new window
        """
        self.root.destroy()
        new_window = Window()

    def end_game(self):
        """
        destroys current window
        """
        self.root.destroy()
