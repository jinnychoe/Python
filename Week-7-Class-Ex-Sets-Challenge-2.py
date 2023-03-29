#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Sets Dictionaries Challenge #2

#create a GUI with some listbox items 
#import all the tkinter pack
from tkinter import*

#create a TK root window named top
top = Tk()

#create listbox object
listbox = Listbox(top,height=10, width=15,bg="grey",activestyle='dotbox', font="Helvita",fg="yellow",selectmode=MULTIPLE)

#define the size of the window
top.geometry('300x250')

#define the label for the list
label= Label(top,text="Food Items")

#insert elements by index with their names as parameters
listbox.insert(1,"Sandwich")
listbox.insert(2,"Burger")
listbox.insert(3,"Pizza")
listbox.insert(4,"French Fries")
listbox.insert(5,"Hot Dogs")
listbox.insert(6,"Cheeseburger")

#create empty list
selected_items=[]

#Function to print the selected value from the listbox
def selected_item():
    
    for i in listbox.curselection():
        #Traverse the tuple return by curselection method and print corresponding values
        selected_items.append(listbox.get(i))
    print(selected_items)
#create a bottom widget and map the command parameter to selected_item function
btn = Button(top,text="Print Selection", command=selected_item)

#pack the widgets
label.pack()
listbox.pack()
btn.pack()

#display until user exits themselves
top.mainloop()
