#Jinny Choe
#5/9/2023
#Week 12 Class Ex Challege 4

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        #create a button widget click me
        #do_something method executed when user clicks button
        self.button1 = tkinter.Button(self.main_window,text='Quote 1',command=self.quote_1)
        self.button2 = tkinter.Button(self.main_window,text='Quote 2',command=self.quote_2)
        self.button3 = tkinter.Button(self.main_window,text='Quote 3',command=self.quote_3)
        
        #pack buttons 
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
    
    #do_something method is call back fxn for button widget 
    def quote_1(self):
        #display info dialog box
        tkinter.messagebox.showinfo('Jinny\'s Quote','Without ice cream, there would be chaos and darkness.')
    def quote_2(self):
        #display info dialog box
        tkinter.messagebox.showinfo('Jinny\'s Quote','When things go wrong, don\'t go with them.')
    def quote_3(self):
        #display info dialog box
        tkinter.messagebox.showinfo('Jinny\'s Quote','Inspiration does exist, but it must find you working.')
        
#create instance of MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
