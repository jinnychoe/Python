
#Jinny Choe
#5/8/2023
#Week 12 Class Ex Project #3
import tkinter

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        #create a label widge containing the text 'hello world'
        self.label = tkinter.Label(self.main_window, text = 'Hello World!')
        
        #call the label widget's pack method
        self.label.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()
        
#create an instance of the MyGUI clas
if __name__ == '__main__':
    gui = MyGUI()
