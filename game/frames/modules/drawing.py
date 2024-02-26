class Draw:
    """
    draws symbols on the board and highlights combinations
    """

    def __init__(self, canvas):
        self.canvas = canvas
        self.line_color = "white"
        self.line_width = 15

    @staticmethod
    def highlight_winning_combination(combination, canvases):
        """
        highlights combination in red
        :param combination: winning combination
        :param canvases: canvases with drawn X or 0
        :return: highlighted winning combination
        """
        if combination:
            for row, col in combination:
                canvases[row][col].config(bg="red")

    def draw_X(self):
        """
        draws X symbol
        :return: "X" string
        """
        self.canvas.create_line(
            20, 20, 120, 120, width=self.line_width, fill=self.line_color
        )
        self.canvas.create_line(
            20, 120, 120, 20, width=self.line_width, fill=self.line_color
        )
        return "X"

    def draw_O(self):
        """
        draws O symbol
        :return: "0" string
        """
        self.canvas.create_oval(
            20, 20, 120, 120, width=self.line_width, outline=self.line_color
        )
        return "O"
