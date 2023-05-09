
#Jinny Choe
#5/8/2023
#Week 12 Class Ex Project 6

#external padding
import tkinter

class MyGUI:
    def __init__(self):
        #create main window widget
        self.main_window = tkinter.Tk()

        #create 2 label widget with solid borders
        self.label1=tkinter.Label(self.main_window,text='Hello World.',borderwidth=1,relief='solid')
        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI program.',borderwidth=1,relief='solid')
        
        #display labels iwth 20 px of horizontal & vertical padding
        self.label1.pack(padx=20, pady=20)
        self.label2.pack(padx=20, pady=20)
      
        #enter the tkinter main loop
        tkinter.mainloop()

#create instance of MyGUI class
if __name__=='__main__':
    my_gui = MyGUI()