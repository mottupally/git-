import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from plyer import notification  # For desktop notifications
import winsound
from threading import Thread

# Initialize the window
window = Tk()
window.geometry('600x600')  # Set size
window.title('PythonGeeks')  # Set title

# Set up labels and entry fields
head = Label(window, text="Countdown Clock and Timer", font=('Calibri 15'))
head.pack(pady=20)
Label(window, text="Enter time in HH:MM:SS", font=('bold')).pack()

# Initialize variables
hour = StringVar()
minute = StringVar()
second = StringVar()
check = BooleanVar()

# Create Entry fields for hours, minutes, seconds
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minute, width=30).pack()
Entry(window, textvariable=second, width=30).pack()

# Create a checkbox for music
Checkbutton(window, text='Check for Music', onvalue=True, variable=check).pack()

# Create a button to start the countdown
def countdown():
    # Convert the entered time into seconds
    try:
        total_seconds = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except ValueError:
        Label(window, text="Please enter valid time!", font=('bold', 12), fg="red").pack()
        return

    # Update countdown display
    def update_timer():
        if total_seconds >= 0:
            mins, secs = divmod(total_seconds, 60)
            display = '{:02d}:{:02d}'.format(mins, secs)
            timer_label.config(text=display)
            total_seconds -= 1
            window.after(1000, update_timer)  # Call the function every 1 second
        else:
            timer_label.config(text="Time's Up!")
            if check.get():
                winsound.Beep(440, 1000)  # Beep sound when time is up
            notification.notify(title="Timer", message="Your countdown has finished!", timeout=10)  # Desktop notification

    # Start the countdown in a new thread to avoid blocking the UI
    Thread(target=update_timer).start()

# Timer label
timer_label = Label(window, text="00:00:00", font=('Calibri', 20), fg='blue')
timer_label.pack(pady=20)

# Set the current time label
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time).pack()

# Start the countdown when the button is clicked
Button(window, text="Set Countdown", command=countdown, bg='yellow').place(x=260, y=230)

# Run the GUI
window.mainloop()
