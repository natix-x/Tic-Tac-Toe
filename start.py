from tkinter import Label, Entry, Button, messagebox
from settings import Settings
import random
from menu import Menu
from board import Board
from title import Title


class Start:
    def __init__(self, menu_frame, board_frame, title_frame):
        self.board_frame = board_frame
        self.menu_frame = menu_frame
        self.title_frame = title_frame
        self.label_font = ("Arial", 13)

        self.name_players_label = Label(
            self.board_frame,
            text="Insert players' nicknames:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=("Arial", 15),
        )
        self.player_X_label = Label(
            self.board_frame,
            text="X:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=self.label_font,
        )
        self.player_O_label = Label(
            self.board_frame,
            text="O:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=self.label_font,
        )
        self.player_X_entry = Entry(self.board_frame, font=self.label_font)
        self.player_O_entry = Entry(self.board_frame, font=self.label_font)
        self.start_button = Button(
            self.board_frame,
            text="Start",
            bg=Settings.background_color,
            fg=Settings.text_color,
            font=self.label_font,
            command=lambda: self.start_game(),
        )
        self.starting_screen()
        self.player_X_name = None
        self.player_O_name = None
        self.chosen_player = None

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
        Wrong nicknames mean:
        1. No nicknames
        2. The same nicknames for both players
        :return: board and right menu
        # TODO player's nickname has to have less than x characters (x I will figure out later)
        # TODO do sth about spaces (change to one or 0 ? in the middle???)
        # TODO create new function
        """
        self.player_X_name = self.player_X_entry.get().strip()
        self.player_O_name = self.player_O_entry.get().strip()
        if self.player_X_name == "" or self.player_O_name == "":
            self.show_error_message("Insert players' nicknames")
        elif self.player_X_name == self.player_O_name:
            self.show_error_message("Players' nicknames cannot be the same")
        else:
            self.destroy_widget(self.board_frame)
            self.drawing_first_player()
            self.board_frame.after(2000, self.initialize_board_and_menu)

    def drawing_first_player(self):
        """
        draws which player will start the game
        :return: drawn player's nickname
        """
        self.chosen_player = random.choice([self.player_X_name, self.player_O_name])
        drawing_label = Label(
            self.board_frame,
            text=f"First player:",
            fg=Settings.text_color,
            background=Settings.background_color,
            font=("Arial", 20),
        )
        drawing_label.place(relx=0.6, rely=0.3, anchor="center")

        drawing_label = Label(
            self.board_frame,
            text=self.chosen_player,
            fg=Settings.text_color,
            background=Settings.background_color,
            font=("Arial", 35),
        )
        drawing_label.place(relx=0.6, rely=0.5, anchor="center")
        self.board_frame.after(2000, lambda: self.destroy_widget(self.board_frame))

    def initialize_board_and_menu(self):
        """
        displays game board, menu and board with players' nicknames assigned to O and X symbols
        :return: game board, menu and updated title frame
        """
        right_menu = Menu(self.menu_frame, self.define_first_player())
        board = Board(self.board_frame, right_menu)
        right_menu.restart_button(board)
        Title(
            self.title_frame,
            player_X_name=self.player_X_name,
            player_O_name=self.player_O_name,
        ).player_board_update()

    @staticmethod
    def destroy_widget(frame):
        """
        destroys widgets present on the frame
        """
        for widget in frame.winfo_children():
            widget.destroy()

    @staticmethod
    def show_error_message(message):
        """
        displays error messagebox
        :param message: message to be displayed
        :return: messagebox
        """
        messagebox.showinfo("Error", message=message)

    def define_first_player(self):
        """
        assigns chosen player's nickname to "X" or "O" symbol to define which sign will first be placed
        :return: str: "X" or "O"
        """
        if self.chosen_player == self.player_X_name:
            return "X"
        else:
            return "O"
