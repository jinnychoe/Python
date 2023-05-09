#Jinny Choe
#5/8/2023
#Week 12 Class Ex Project #2
import tkinter

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        #display a title
        self.main_window.title('My First GUI')
        
        #Enter the tkinter main loop
        tkinter.mainloop()
        
#create an instance of the MyGUI clas
if __name__ == '__main__':
    gui = MyGUI()