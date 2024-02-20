from tkinter import Button, Canvas, messagebox
from game_logic import GameLogic
from drawing import Draw
from settings import Settings


class Board:
    def __init__(self, localization, menu):
        self.localization = localization
        self.menu = menu
        self.current_player = "X"
        self.buttons = [[" " for _ in range(3)] for _ in range(3)]
        self.canvas = None
        self.canvases = [[None for _ in range(3)] for _ in range(3)]
        self.buttons_initiation()

    def buttons_initiation(self):
        """
        creates buttons on the board
        :return: Buttons matrix (3 x 3)
        """
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(
                    self.localization,
                    text=" ",
                    height=9,
                    width=20,
                    command=lambda row=i, col=j: self.make_move(row, col),
                    background="black",
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        """
        draws X or 0 symbol on the board where player clicked;
        if current player won: highlights winning combination,
        updates scoreboard and gives players possibility to restart board;
        elif a tie: gives players possibility to restart board;
        else: changes current player
        :param row: row of the button clicked by player
        :param col: column of the button clicked by player
        :return: updated board
        """
        if self.buttons[row][col]["text"] == " ":
            self.canvases[row][col] = Canvas(
                self.localization,
                width=Settings.root_width * 0.25 - 10,
                height=Settings.root_width * 0.25 - 10,
                background=Settings.background_color,
                highlightthickness=0,
            )
            self.canvas = self.canvases[row][col]
            drawing = Draw(self.canvas)
            if self.current_player == "X":
                self.buttons[row][col].config(text=drawing.draw_X())
            else:
                self.buttons[row][col].config(text=drawing.draw_0())

            self.canvases[row][col].grid(row=row, column=col)

            game_logic = GameLogic(self.buttons)
            winning_combination = game_logic.check_if_win()

            if winning_combination:
                drawing.highlight_winning_combination(
                    winning_combination, self.canvases
                )
                self.menu.update_scoreboard(winner=self.current_player)
                self.handle_restart(
                    f"Player {self.current_player} wins!", self.canvases
                )
            elif game_logic.check_if_tie():
                self.handle_restart("Tie!", self.canvases)

            self.current_player = "O" if self.current_player == "X" else "X"

    def restart_board(self, canvases):
        """
        restarts board
        :param canvases: canvases empty or with drawn X or 0 present on the board
        :return:
        """
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
                if canvases[i][j] is not None:
                    canvases[i][j].destroy()

    def handle_restart(self, message, canvases):
        """
        displays the message (winning or tie information) and asks if player wants to restart the game (board)
        :param message: message to display on the messagebox after winning or tie
        :param canvases: canvases empty or with drawn X or 0 present on the board
        """
        restart = messagebox.askyesno(
            "Game Over",
            f"{message} Do you want to restart?",
            icon="question",
            default="yes",
        )
        if restart:
            self.restart_board(canvases)
