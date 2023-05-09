
#Jinny Choe
#5/8/2023
#Week 12 Class Ex Project 4
import tkinter

class MyGUI:
    def __init__(self):
        #create main window widget
        self.main_window = tkinter.Tk()

        #create 2 label widget
        self.label1=tkinter.Label(self.main_window,text='Hello World')
        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI program.')

        #call both label widgets' pack method
        self.label1.pack()
        self.label2.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

#create instance of MyGUI class
if __name__=='__main__':
    my_gui = MyGUI()