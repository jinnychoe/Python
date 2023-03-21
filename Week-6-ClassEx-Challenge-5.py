# Jinny Choe
# 3/21/2023
# Week 6 Class Exercise Challenge #5

import tkinter as tk  # import the gui interface controls
from tkinter import messagebox  # imports the messagebox display

win = tk.Tk()  # creates window interface
win.geometry("400x200")  # width x height in pixels
win.title("Customer Information")  # label for the title

lblLastname = tk.Label(win, text="enter the last name: ").grid(column=0, row=0)  # label widget
lblFirstname = tk.Label(win, text="enter the first name: ").grid(column=0, row=1)
lblAddress = tk.Label(win, text="Address: ").grid(column=0, row=2)
lblCity = tk.Label(win, text="City: ").grid(column=0, row=3)
lblState = tk.Label(win, text="State: ").grid(column=0, row=4)
lblZipcode = tk.Label(win, text="Zipcode: ").grid(column=0, row=5)



def write():
    text_file = open("Customers.txt", "a")
    content = text_file.write("\nConfirmation: " + str(LN.get()) + ", " + str(FN.get())+ "," + str(ADDRESS.get()) + "," + str(CITY.get()) + "," + str(STATE.get()) + "," + str(ZIPCODE.get()))
    text_file.close()
    messagebox.showinfo("Information", "Data recorded")


def quit():
    messagebox.showinfo("Information", "Thank you...")
    win.destroy()  # closes interface


def submit():  # function name
    messagebox.showinfo("Information", "Entered: " + LN.get() + "," + FN.get()  + "," + ADDRESS.get() + "," + CITY.get() + "," + STATE.get() + "," + ZIPCODE.get())  # display info


LN = tk.StringVar()  # the StringVar manages the entry widget
txtLastname = tk.Entry(win, width=12, textvariable=LN).grid(column=1, row=0)  # text entry widget

FN = tk.StringVar()
txtFirstname = tk.Entry(win, width=12, textvariable=FN).grid(column=1, row=1)

ADDRESS = tk.StringVar()
txtAddress = tk.Entry(win, width=35, textvariable=ADDRESS).grid(column=1, row=2)

CITY = tk.StringVar()
tk.Entry(win, width=35, textvariable=CITY).grid(column=1, row=3)

STATE = tk.StringVar()
tk.Entry(win, width=35, textvariable=STATE).grid(column=1, row=4)

ZIPCODE = tk.StringVar()
tk.Entry(win, width=35, textvariable=ZIPCODE).grid(column=1, row=5)



# command calls the click fxn
btnSubmit = tk.Button(win, text="Submit", command=submit).grid(column=0, row=4)  # Button widget

# command calls quit fxn
btnQuit = tk.Button(win, text="Quit", command=quit).grid(column=1, row=4)  # button widget

# call the function write
btnWrite = tk.Button(win, text="Transfer", command=write).grid(column=1, row=4)  # button widget

win.mainloop()  # ensures ethe interfaces stays on the screen or window
