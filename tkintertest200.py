import tkinter
from tkinter import Button, Label, messagebox
import random
from random import randint
from tkinter.constants import COMMAND, YES


tk = tkinter.Tk()
tk.geometry('450x450')
tk.title('Guess the number!')
low = 1
high = 100
#Counts the guesses
guess_count = 0
#Randomizes a number from 1 to 100
rand = randint(low,high)
def thestartofthegame():
    global rand      
    rand = randint(low,high)
    #Print attempts. After every attempt it will plus 1 to the overall attempt's value.
    Label=tkinter.Label(tk,text=f"Attempts:{guess_count}")
    Label.grid(column=3,row=3)
def check(guess):
    global guess_count
    global entry
    if guess < rand:
        Label=tkinter.Label(tk,text=f"You guessed: {guess} The right number is HIGHER than that")
        Label.grid(column=3,row=0)
        guess_count = guess_count+1
        Label=tkinter.Label(tk,text=f"Attempts:{guess_count}")
        Label.grid(column=3,row=3)
        entry.destroy()
        entry = tkinter.Entry(tk)
        entry.grid(column=3,row=1)
    elif guess > rand:
        Label=tkinter.Label(tk,text=f"You guessed: {guess} The right number is LOWER than that")
        Label.grid(column=3,row=0)
        guess_count = guess_count+1
        Label=tkinter.Label(tk,text=f"Attempts:{guess_count}")
        Label.grid(column=3,row=3)
        entry.destroy()
        entry = tkinter.Entry(tk)
        entry.grid(column=3,row=1)
    else:
        result = messagebox.askquestion("Correct!", f"You WON! Number {guess} is correct and you tried {guess_count} times, do you want to try again?")
        if result == "yes":
            #If player presses yes, the game will start again.
            thestartofthegame()
            entry.destroy()
            entry = tkinter.Entry(tk)
            entry.grid(column=3,row=1)
            guess_count = 0
        else:
            #Else game ends.
            tk.destroy()



entry = tkinter.Entry(tk)
entry.grid(column=3,row=1)

button=tkinter.Button(tk, text="My guess", command=lambda: check(int(entry.get())))
button.bind("<Return>", check(int(entry.get())))
button.grid(column=3,row=2)





tk.mainloop()