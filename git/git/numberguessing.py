import tkinter as tk
from tkinter import *
import random

# Initialize the Tkinter window
win = tk.Tk()
win.geometry("750x750")
win.title("PythonGeeks")

# Declare variables
guess = IntVar()
hint = StringVar()
score = IntVar()
final_score = IntVar()

# Random number to guess
num = random.randint(1, 50)

# Set initial values
hint.set("Guess a number between 1 to 50")
score.set(5)
final_score.set(score.get())

# Function to check the guess
def fun():
    x = guess.get()  # Get the value entered in the guess Entry
    if score.get() > 0:
        if x > 50 or x < 1:  # Check if guess is out of valid range
            hint.set("You just lost 1 Chance. Guess a number between 1 and 50.")
            score.set(score.get() - 1)
            final_score.set(score.get())

        elif num == x:  # Check if the guess is correct
            hint.set("Congratulations! YOU WON!!!")
            score.set(score.get() - 1)
            final_score.set(score.get())

        elif num > x:  # Guess is too low
            hint.set("Your guess was too low. Guess a number higher.")
            score.set(score.get() - 1)
            final_score.set(score.get())

        elif num < x:  # Guess is too high
            hint.set("Your guess was too high. Guess a number lower.")
            score.set(score.get() - 1)
            final_score.set(score.get())

    else:
        hint.set("Game Over! You Lost.")

# Create UI elements
Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

# Entry for user's guess
Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)

# Entry for the hint
Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)

# Entry for displaying final score
Entry(win, textvariable=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

# Button to check the guess
Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

# Start the Tkinter main loop
win.mainloop()
