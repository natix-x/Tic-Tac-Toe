class GameLogic:
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
                self.buttons[i][(2 - i)]["text"] != " "
                and self.buttons[i][(2 - i)]["text"]
                == self.buttons[(i + 1) % 3][2 - (i + 1) % 3]["text"]
                == self.buttons[(i + 2) % 3][2 - (i + 2) % 3]["text"]
            ):
                return [
                    (i, 2 - i),
                    (i + 1, 2 - (i + 1)),
                    (i + 2, 2 - (i + 2)),
                ]  # return first winning diagonal
            elif (
                self.buttons[i][i]["text"] != " "
                and self.buttons[i][i]["text"]
                == self.buttons[(i + 1) % 3][(i + 1) % 3]["text"]
                == self.buttons[(i + 2) % 3][(i + 2) % 3]["text"]
            ):
                return [
                    (i, i),
                    (i + 1, i + 1),
                    (i + 2, i + 2),
                ]  # return second winning diagonal

        return None

    def check_if_tie(self):
        """
        checks if tie
        "tie" means no same three symbols in one row/column/diagonal
        """
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                    return False
        return True
