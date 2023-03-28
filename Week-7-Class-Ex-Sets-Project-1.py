#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Sets Dictionaries Project 3

#Import tkinter
from tkinter import *

#create the root window
root = Tk()
root.geometry('180x200')

#create a listbox
listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)

#Inserting the listbox items
listbox.insert(1, "Data Structure")
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(4, "Machine Learning")
listbox.insert(5, "Blockchain")

#Function for printing the selected listbox values
def selected_item():
    
    #traverse the tuple returned by curselection method and print corresponding values(s) in the listbox
    for i in listbox.curselection():
        print(listbox.get(i))
    
#create a button widget to map the command parameter to selected_item function
btn = Button(root, text='Print Selected', command=selected_item)
    
#placing the button and listbox
btn.pack(side='bottom')
listbox.pack()
    
root.mainloop()