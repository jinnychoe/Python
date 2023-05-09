
#Jinny Choe
#5/8/2023
#Week 12 Class Ex Challenge #2
import tkinter

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        self.last_name_label = tkinter.Label(self.main_window, text='Last Name: ')
        self.last_name_label.pack()

        self.first_name_label = tkinter.Label(self.main_window, text = 'First name: ')
        self.first_name_label.pack()

        self.age_label = tkinter.Label(self.main_window, text='Age: ')
        self.age_label.pack()



        #Enter the tkinter main loop
        tkinter.mainloop()
        
#create an instance of the MyGUI clas
if __name__ == '__main__':
    gui = MyGUI()
