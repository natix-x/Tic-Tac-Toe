from tkinter import messagebox


class NicknamesErrorsHandler:
    """
    handler for nicknames errors (players' mistakes)
    """

    def __init__(self, player_X_name, player_O_name):
        self.player_X_name = player_X_name
        self.player_O_name = player_O_name

    @staticmethod
    def show_error_message(message):
        """
        displays error messagebox
        :param message: message to be displayed
        :return: messagebox
        """
        messagebox.showinfo("Error", message=message)

    def error_occurrence(self):
        """
        returns True if wrong nicknames:
        1. No nickname or n
        2. The same nicknames for both players
        3. Nickname has more than 10 characters
        else: returns False
        """
        players = [self.player_X_name, self.player_O_name]
        for player in players:
            if player == "":
                self.show_error_message("Insert all players' nicknames")
                return True
            elif len(player) > 10:
                self.show_error_message("Nicknames should have less than 11 characters")
                return True
        if players[0] == players[1]:
            self.show_error_message("Players' nicknames cannot be the same")
            return True
        return False
