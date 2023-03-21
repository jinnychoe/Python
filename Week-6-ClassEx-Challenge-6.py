# Jinny Choe
# 3/21/2023
# Week 6 Class Exercise Challenge #6

import tkinter as tk    # import the gui interface controls
from tkinter import messagebox      #imports the messagebox display

win = tk.Tk()   #creates window interface
win.geometry("400x400")     #width x height in pixels
win.title("Numbers")    #label for the title

lblnum1 = tk.Label(win, text="Enter first number: ").grid(column=0, row=0)      #label widget
lblnum2 = tk.Label(win, text="Enter second number: ").grid(column=0, row=1)
lblnum3 = tk.Label(win, text="Enter third number: ").grid(column=0, row=2)

NUM1 = tk.StringVar()  # the StringVar manages the entry widget
txtNum1 = tk.Entry(win, width=10, textvariable=NUM1).grid(column=1, row=0)      #text entry widget

NUM2 = tk.StringVar()
txtNum2 = tk.Entry(win, width=10, textvariable=NUM2).grid(column=1, row=1)

NUM3 = tk.StringVar()
txtNum3 = tk.Entry(win, width=10, textvariable=NUM3).grid(column=1, row=2)

def write():
    TOTAL = float(NUM1.get())+float(NUM2.get())+float(NUM3.get()) #get total value
    AVG = TOTAL/3 #get average value
    
    messagebox.showinfo("Calculations", "The sum is "+str(TOTAL) +". The average is "+str(AVG))
   
    text_file = open("Numbers.txt", "a") #open text file to append
 
    #write in text file
    content = text_file.write("\nThe three numbers are: "+ str(NUM1.get()) + ", " + str(NUM2.get())+ "," + str(NUM3.get())+"\nThe total is " +(TOTAL)+ ".\n The average is " + str(AVG) + ".")
   
    text_file.close() #close text file
    
    messagebox.showinfo("Numbers", "Data recorded in Numbers.txt.")
    
def quit(): #quit fxn
    messagebox.showinfo("Numbers", "Thank you...")
    win.destroy()  # closes interface

def submit():  #function name
    messagebox.showinfo("Numbers", "Entered: " + NUM1.get() + "," + NUM2.get()  + "," + NUM3.get())  # display info
    
#command calls the click fxn
btnSubmit = tk.Button(win, text="Submit", command=submit).grid(column=0, row=4)  # Button widget

#command calls quit fxn
btnQuit = tk.Button(win, text="Quit", command=quit).grid(column=1, row=4)  # button widget

#call the function write
btnWrite = tk.Button(win, text="Transfer", command=write).grid(column=1, row=4)  # button widget



win.mainloop()  # ensures the interfaces stays on the screen or window
