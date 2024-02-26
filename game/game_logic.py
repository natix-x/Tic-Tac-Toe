class GameLogic:
    """
    defines winning and tie cases and checks if any of them are present on the game board
    """

    def __init__(self, buttons):
        self.buttons = buttons

    def check_if_win(self):
        """
        checks if won.
        Possible winning combinations:
        1. Three same symbols in one row
        2. Three same symbols in one column
        3. Three same symbols in one diagonal
        :return: winning combination
        """
        for i in range(3):
            for j in range(3):
                if (
                    self.buttons[i][j]["text"] != " "
                    and self.buttons[i][j]["text"]
                    == self.buttons[i][(j + 1) % 3]["text"]
                    == self.buttons[i][(j + 2) % 3]["text"]
                ):
                    return [(i, 0), (i, 1), (i, 2)]  # return winning row
                elif (
                    self.buttons[i][j]["text"] != " "
                    and self.buttons[i][j]["text"]
                    == self.buttons[(i + 1) % 3][j]["text"]
                    == self.buttons[(i + 2) % 3][j]["text"]
                ):
                    return [(0, j), (1, j), (2, j)]  # return winning column
            if (
                self.buttons[0][0]["text"] != " "
                and self.buttons[0][0]["text"]
                == self.buttons[1][1]["text"]
                == self.buttons[2][2]["text"]
            ):
                return [(0, 0), (1, 1), (2, 2)]  # return first diagonal
            elif (
                self.buttons[0][2]["text"] != " "
                and self.buttons[0][2]["text"]
                == self.buttons[1][1]["text"]
                == self.buttons[2][0]["text"]
            ):
                return [(0, 2), (1, 1), (2, 0)]  # return second diagonal

        return None

    def check_if_tie(self):
        """
        checks if tie
        "tie" means no same three symbols in one row/column/diagonal
        :return: True if a tie, else: False
        """
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                    return False
        return True
