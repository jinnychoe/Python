
#Jinny Choe
#5/8/2023
#Week 12 Class Ex Project 

#button
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #create main window widget
        self.main_window = tkinter.Tk()

        #create button widget. 'Click me' should appear on face of button
        #do_something method executed when user clicks button

        self.my_button = tkinter.Button(self.main_window,text='Click Me!',command=self.do_something)

        #pack the button
        self.my_button.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

    def do_something(self):
        #display info dialog box
        tkinter.messagebox.showinfo('Response','Thanks for clicking the button.')

#create instance of MyGUI class
if __name__=='__main__':
    my_gui = MyGUI()