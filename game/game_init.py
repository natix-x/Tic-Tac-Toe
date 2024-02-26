from tkinter import Label, Entry, Button
from frames.modules.settings import Settings
import random
from frames.menu import Menu
from frames.board import Board
from frames.title import Title
from frames.modules.nicknames_errors_handler import NicknamesErrorsHandler
import re


class GameInit:
    """
    initializes game, handles following functionalities: inserting by player nicknames, drawing the first player,
    initialize_board_and_menu
    """

    def __init__(self, window_instance):
        self.window_instance = window_instance
        self.label_font = ("Arial", 13)
        self.name_players_label = Label(
            self.window_instance.board_frame,
            text="Insert players' nicknames:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=("Arial", 15),
        )
        self.player_X_label = Label(
            self.window_instance.board_frame,
            text="X:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=self.label_font,
        )
        self.player_O_label = Label(
            self.window_instance.board_frame,
            text="O:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=self.label_font,
        )
        self.player_X_entry = Entry(
            self.window_instance.board_frame, font=self.label_font
        )
        self.player_O_entry = Entry(
            self.window_instance.board_frame, font=self.label_font
        )
        self.start_button = Button(
            self.window_instance.board_frame,
            text="Start",
            bg=Settings.background_color,
            fg=Settings.text_color,
            font=self.label_font,
            command=lambda: self.start_game(),
        )
        Title(self.window_instance.title_frame)
        self.starting_screen()
        self.player_X_name = None
        self.player_O_name = None
        self.chosen_player = None

    @staticmethod
    def destroy_widget(frame):
        """
        destroys widgets present on the frame
        """
        for widget in frame.winfo_children():
            widget.destroy()

    def starting_screen(self):
        """
        displays starting screen. Players can choose their nicknames and decide who represents which sign.
        :return: starting screen
        """
        self.name_players_label.grid(
            row=0, column=0, columnspan=2, pady=(120, 20), padx=10
        )
        self.player_X_label.grid(row=1, column=0, sticky="e", padx=(150, 0))
        self.player_X_entry.grid(row=1, column=1, pady=20, padx=(0, 150))
        self.player_O_label.grid(row=2, column=0, sticky="e", padx=(150, 0))
        self.player_O_entry.grid(row=2, column=1, pady=20, padx=(0, 150))
        self.start_button.grid(row=3, column=0, columnspan=2, pady=(20, 40), padx=10)

    def start_game(self):
        """
        destroys starting screen, displays drawn player and initialize board and menu.
        If wrong nicknames inserted displays error message.
        :return: board and right menu
        """
        self.player_X_name = self.player_X_entry.get().strip()
        self.player_X_name = re.sub("\s\s+", " ", self.player_X_name)
        # change many inserted by player spaces to one space
        self.player_O_name = self.player_O_entry.get().strip()
        self.player_O_name = re.sub("\s\s+", " ", self.player_O_name)
        # change many inserted by player spaces to one space

        errors_check = NicknamesErrorsHandler(self.player_X_name, self.player_O_name)

        if errors_check.error_occurrence() is False:
            self.destroy_widget(self.window_instance.board_frame)
            self.drawing_first_player()
            self.window_instance.board_frame.after(2000, self.initialize_board_and_menu)
        else:
            self.starting_screen()

    def drawing_first_player(self):
        """
        draws which player will start the game
        :return: drawn player's nickname
        """
        self.chosen_player = random.choice([self.player_X_name, self.player_O_name])
        drawing_label = Label(
            self.window_instance.board_frame,
            text=f"First player:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=("Arial", 20),
        )
        drawing_label.place(relx=0.6, rely=0.3, anchor="center")

        drawing_label = Label(
            self.window_instance.board_frame,
            text=self.chosen_player,
            fg=Settings.text_color,
            background=Settings.background_color,
            font=("Arial", 35),
        )
        drawing_label.place(relx=0.6, rely=0.5, anchor="center")
        self.window_instance.board_frame.after(
            2000, lambda: self.destroy_widget(self.window_instance.board_frame)
        )

    def initialize_board_and_menu(self):
        """
        displays game board, menu and board with players' nicknames assigned to O and X symbols
        :return: game board, menu and updated title frame
        """
        right_menu = Menu(
            self.window_instance.menu_frame,
            first_player=self.define_first_player(),
            game_instance=self,
        )
        board = Board(self.window_instance.board_frame, right_menu)
        right_menu.restart_button(board)
        Title(
            self.window_instance.title_frame,
            player_X_name=self.player_X_name,
            player_O_name=self.player_O_name,
        ).players_board_update()

    def define_first_player(self):
        """
        assigns chosen player's nickname to "X" or "O" symbol to define which sign will first be placed
        :return: str: "X" or "O"
        """
        if self.chosen_player == self.player_X_name:
            return "X"
        else:
            return "O"
