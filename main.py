import tkinter as tk
from tkinter import *
from tkinter import font
import logic

WINDOW_BACKGROUND = "#24242A"
TEXT_COLOR = "#F9E6A9"
root = Tk()
root.title("Text Adventure")
root.config(bg=WINDOW_BACKGROUND)

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="High Tower Text", size=12)

game_frame = Frame(root, bg="#64463F")
game_frame.grid(row=0, column=0)

scrollbar = Scrollbar(root, bg=WINDOW_BACKGROUND)
scrollbar.grid(row=0, column=3, rowspan=2, sticky=NS)

text_field = Text(game_frame, yscrollcommand=scrollbar.set)
text_field.config(bg="#64463F", fg=TEXT_COLOR, font=("High Tower Text", 14, "bold"), border=0)
text_field.insert(END, "Press ENTER to start!")
text_field.config(state=DISABLED)
text_field.grid(row=0, column=0, padx=5, pady=5)
scrollbar.config(command=text_field.yview)

with open("story.txt", mode="r") as story:
    story_text = story.readlines()

input_frame = Frame(root, bg=WINDOW_BACKGROUND)
input_frame.grid(row=1, column=0, sticky=EW)

input_label = Label(input_frame, text="Type Here: ")
input_label.config(bg=WINDOW_BACKGROUND, fg=TEXT_COLOR)
input_label.grid(row=0, column=0, padx=10)


# SETUP ENTRY FIELD FOR USER INPUT
def callback(var):
   content = var.get()


var = StringVar()
var.trace("w", lambda name, index,mode, var=var: callback(var))
input_field = Entry(input_frame, textvariable=var, state=DISABLED, bg="#41414D", fg=TEXT_COLOR, disabledbackground=WINDOW_BACKGROUND)
input_field.grid(row=0, column=1, sticky=NSEW)
input_frame.columnconfigure(1, weight=1)


# START GAME
root.bind("<Return>", lambda event: logic.start_game(text_field, input_field))


def on_closing():
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
