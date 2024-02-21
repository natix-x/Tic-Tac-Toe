from tkinter import Label, Entry, Button, messagebox
from settings import Settings
from menu import Menu
from board import Board
import random


class Start:
    def __init__(self, menu_frame, board_frame):
        self.board_frame = board_frame
        self.menu_frame = menu_frame
        self.font = ("Arial", 13)

        self.name_players_label = Label(self.board_frame, text="Insert players' nicknames:", fg=Settings.text_color,
                                        background=Settings.background_color, font=("Arial", 15))
        self.player_one_label = Label(self.board_frame, text="X:", fg=Settings.text_color,
                                      background=Settings.background_color, font=self.font)
        self.player_two_label = Label(self.board_frame, text="O:", fg=Settings.text_color,
                                      background=Settings.background_color, font=self.font)
        self.player_one_entry = Entry(self.board_frame, font=self.font)
        self.player_two_entry = Entry(self.board_frame, font=self.font)
        self.start_button = Button(self.board_frame, text="Start", bg=Settings.background_color,
                                   fg=Settings.text_color, font=self.font, command=lambda: self.start_game())

        self.starting_screen()

    def starting_screen(self):
        """
        displays starting screen. Players can choose their nicknames and decide who represents which sign.
        :return: starting screen
        """
        self.name_players_label.grid(row=0, column=0, columnspan=2, pady=(120, 20), padx=10)
        self.player_one_label.grid(row=1, column=0, sticky="e", padx=(150, 0))
        self.player_one_entry.grid(row=1, column=1, pady=20, padx=(0, 150))
        self.player_two_label.grid(row=2, column=0, sticky="e", padx=(150, 0))
        self.player_two_entry.grid(row=2, column=1, pady=20, padx=(0, 150))
        self.start_button.grid(row=3, column=0, columnspan=2, pady=(20, 40), padx=10)

    def start_game(self):
        """
        destroys starting_screen and displays interactive board and right menu.
        If no nicknames inserted or just one displays error message
        :return: board and right menu
        # TODO player's nickname has to have less than x characters (x I will figure out later)
        """
        if (self.player_one_entry.get()) == "" or (self.player_two_entry.get() == ""):
            self.show_error_message("Insert players' nicknames")
        elif self.player_one_entry.get() == self.player_two_entry.get():
            self.show_error_message("Players' nicknames cannot be the same")
        else:
            self.draw_first_player()
            for widget in self.board_frame.winfo_children():
                widget.destroy()
            right_menu = Menu(self.menu_frame)
            board = Board(self.board_frame, right_menu)
            right_menu.restart_button(board)

    def draw_first_player(self):
        pass

    @staticmethod
    def show_error_message(message):
        """
        displays error messagebox
        :param message: displayed message
        :return: messagebox
        """
        messagebox.showinfo("Error", message=message)


