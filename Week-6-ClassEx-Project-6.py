# Jinny Choe
# 3/20/2023
# Week 6 Class Exercise Project #6

import tkinter as tk  # import the gui interface controls
from tkinter import messagebox  # imports the messagebox display

win = tk.Tk()  # creates window interface
win.geometry("300x100")  # width x height in pixels
win.title("Customer Information")  # label for the title

lblLastname = tk.Label(win, text="enter the last name: ").grid(column=0, row=0)  # label widget
lblFirstname = tk.Label(win, text="enter the first name: ").grid(column=0, row=1)


def write():
    text_file = open("Customers.txt", "a")
    content = text_file.write("\nConfirmation: " + str(LN.get()) + ", " + str(FN.get()))
    text_file.close()
    messagebox.showinfo("information", "Data recorded")


def quit():
    messagebox.showinfo("information", "Thank you...")
    win.destroy()  # closes interface


def submit():  # function name
    messagebox.showinfo("information", "entered: " + LN.get() + "," + FN.get())  # display info


LN = tk.StringVar()  # the StringVar manages the entry widget
txtLastname = tk.Entry(win, width=12, textvariable=LN).grid(column=1, row=0)  # text entry widget
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width=12, textvariable=FN).grid(column=1, row=1)

# command calls the click fxn
btnSubmit = tk.Button(win, text="submit", command=submit).grid(column=0, row=4)  # Button widget

# command calls quit fxn
btnQuit = tk.Button(win, text="quit", command=quit).grid(column=1, row=4)  # button widget

# call the function write
btnWrite = tk.Button(win, text="transfer", command=write).grid(column=1, row=4)  # button widget

win.mainloop()  # ensures ethe interfaces stays on the screen or window
submit()
