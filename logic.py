from tkinter import *
import time
TEXT_SPEED = 1


def edit_field(func):
    def wrapper(**kwargs):
        if "field" in kwargs:
            kwargs["field"].config(state=NORMAL)
            func(**kwargs)
            kwargs["field"].config(state=DISABLED)
    return wrapper


@edit_field
def clear_field(field: Text):
    field.delete("1.0", END)


@edit_field
def write_field(field: Text, new_text):
    field.insert(END, new_text)


def listen_to_entry(entry: Entry, options: list) -> str:
    """Listens to and waits for changes to the Tkinter Entry Field, will return the choice once the input in the 
    entry field matches with one of the options provided."""
    entry.config(state=NORMAL)
    entry.focus()
    while entry.get().upper() not in options:
        entry.wait_variable(entry.cget("textvariable"))

    choice = entry.get().upper()
    entry.delete(0, END)
    entry.config(state=DISABLED)
    return choice


def start_game(text_field: Text, entry: Entry):

    # OPEN TEXT FILE WITH STORY
    with open("story.txt", mode="r", encoding='UTF8') as text:
        story = text.readlines()

    clear_field(field=text_field)

    # WRITE STORY TEXT
    options = False
    ignore = False
    current_choice = None
    for i, line in enumerate(story):
        
        # IGNORES LINES UNTIL WE REACH THE BLOCK FOR THE CHOSEN OPTION
        if ignore:
            if line.strip() == f"|{current_choice}":
                ignore = False
                write_field(field=text_field, new_text="\n")
                continue
            else:
                continue
        
        # THE NEXT LINE AFTER THIS IS TRUE SHOULD BE OUR OPTIONS
        if line.strip() == "[CHOOSE]":
            options = True
            continue

        if options:
            option_list = [option.strip() for option in line.split(", ")]   
            current_choice = listen_to_entry(entry, option_list)
            ignore = True
            options = False
            continue

        # A MINUS - SYMBOL SIGNIFIES THE END OF OUR GAME
        if line.strip() == "-":
            write_field(field=text_field, new_text="\nGAME END!")
            text_field.see(END)
            break

        # ADDS CHARACTERS ONE AT A TIME TO OUR TEXT FIELD
        for char in line:
            write_field(field=text_field, new_text=char)
            text_field.see(END)
            text_field.after(TEXT_SPEED)
            text_field.update()
    