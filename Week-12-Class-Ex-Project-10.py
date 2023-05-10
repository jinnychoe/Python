#Jinny Choe
#5/9/2023
#Week 12 Class Ex Project 10

#This program has a quit button that calls the Tk class's destroy method when clicked

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        #create a button widget click me
        #do_something method executed when user clicks button
        self.my_button = tkinter.Button(self.main_window,text='Click Me!',command=self.do_something)
        
        #quit button
        #root widget's destroy method called when cliked
        #main_window var references root widget, so callback fxn is self.main_window.destroy
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        
        #pack buttons
        self.my_button.pack()
        self.quit_button.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
    
    #do_something method is call back fxn for button widget
    def do_something(self):
        #display info dialog box
        tkinter.messagebox.showinfo('Response','Thanks for clicking the button.')
    
 #create instance of MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
