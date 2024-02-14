from tkinter import *

root = Tk()

root.configure(bg="#6cc2f0")
root.geometry("600x550")
root.title("Tic Tac Toe")
root.resizable(False, False)

title_frame = Frame(root, bg="#6cc2f0",
 width=600, height=100)
title_frame.place(x=0, y=0)

right_frame = Frame(root, bg="#6cc2f0",
                    width=150, height=450)
right_frame.place(x=450,y=100)

board_frame = Frame(root, bg="#6cc2f0",
                    width=450, height=450
                    )
board_frame.place(x=0, y=100)
root.mainloop()