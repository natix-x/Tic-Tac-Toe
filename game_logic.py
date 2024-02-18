class GameLogic:
    def __init__(self, buttons):
        self.buttons = buttons

    def check_if_win(self):
        for i in range(3):
            if (
                self.buttons[i][0]["text"] != " "
                and self.buttons[i][0]["text"]
                == self.buttons[i][1]["text"]
                == self.buttons[i][2]["text"]
            ):
                return [(i, 0), (i, 1), (i, 2)]  # Return winning row
            elif (
                self.buttons[0][i]["text"] != " "
                and self.buttons[0][i]["text"]
                == self.buttons[1][i]["text"]
                == self.buttons[2][i]["text"]
            ):
                return [(0, i), (1, i), (2, i)]  # Return winning column
        if (
            self.buttons[0][0]["text"] != " "
            and self.buttons[0][0]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][2]["text"]
        ):
            return [(0, 0), (1, 1), (2, 2)]  # Return diagonal
        elif (
            self.buttons[0][2]["text"] != " "
            and self.buttons[0][2]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][0]["text"]
        ):
            return [(0, 2), (1, 1), (2, 0)]  # Return diagonal
        return None

    def check_if_tie(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                    return False
        return True