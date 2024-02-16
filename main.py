from tkinter import *
from board import Board

root = Tk()

root.configure(bg="black")
root.geometry("600x550")
root.title("Tic Tac Toe")
root.resizable(False, False)

title_frame = Frame(root, bg="black", width=600, height=100)
title_frame.place(x=0, y=0)

right_frame = Frame(root, bg="black", width=150, height=450)
right_frame.place(x=450, y=100)

board_frame = Frame(root, bg="black", width=450, height=450)
board_frame.place(x=0, y=100)

b = Board(board_frame)

root.mainloop()
