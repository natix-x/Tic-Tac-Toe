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
                return True
            elif (
                self.buttons[0][i]["text"] != " "
                and self.buttons[0][i]["text"]
                == self.buttons[1][i]["text"]
                == self.buttons[2][i]["text"]
            ):
                return True
        if (
            self.buttons[0][2]["text"] != " "
            and self.buttons[0][2]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][0]["text"]
        ):
            return True
        elif (
            self.buttons[0][0]["text"] != " "
            and self.buttons[0][0]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][2]["text"]
        ):
            diagonal = "left_to_right_down"
            return True, diagonal

    def check_if_tie(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                    return False
        return True
