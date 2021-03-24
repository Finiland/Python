import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageGrab
import random



answer = random.randint(1, 100)
number = random.randint(1, 100)

def check_answer():
    global attempts
    global text
    print(number, answer)

    guess = str(entry_window.get())

    if guess == "b" or guess == "B":
        print("B")
        if number > answer:
            text.set(str(number) + 'your number!' 'You won!')
            btn_check.pack_forget()
        elif number == answer:
            text.set(str(number) + 'your number!' "Tie!")
            btn_check.pack_forget()
        elif answer > number:
            text.set(str(number) + 'your number!' 'You lost!')
            btn_check.pack_forget()
    elif guess == "s" or guess == "S":
        print("S")
        if answer > number:
            text.set(str(number) + 'your number!' 'You won!')
            btn_check.pack_forget()
        elif number == answer:
            text.set(str(number) + 'your number!' "Tie!")
            btn_check.pack_forget()
        elif number > answer:
            text.set(str(number) + 'your number!' "You lost!")
            btn_check.pack_forget()


root = Tk()

root.title('Guess the number!')

root.geometry('500x150')

label = Label(root, text=str(answer) + "   Is the number! Will the next number be bigger or smaller?")
label.pack()

entry_window = Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy)
btn_quit.pack()


text = StringVar()
text.set("Hi! Welcome!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()
root.mainloop()
