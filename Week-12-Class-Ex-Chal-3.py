
#Jinny Choe
#5/8/2023
#Week 12 Class Ex Challenge 3

#internal padding
import tkinter

class MyGUI:
    def __init__(self):
        #create main window widget
        self.main_window = tkinter.Tk()

        #create 2 label widget with solid borders
        self.label1=tkinter.Label(self.main_window,text='Hello World.',borderwidth=1,relief='solid')
        self.label2 = tkinter.Label(self.main_window, text = 'This is Jinny\'s GUI program.',borderwidth=1,relief='solid')
        self.label3 = tkinter.Label(self.main_window, text = 'Never give up. I believe in you. You can do it.',borderwidth=1,relief='solid')
        self.label4 = tkinter.Label(self.main_window, text = 'Just keep swimming.',borderwidth=1,relief='solid')

        #display labels iwth 20 px of horizontal & vertical padding
        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)
        self.label3.pack(ipadx=20, ipady=20)
        self.label4.pack(ipadx=20, ipady=20)

        #enter the tkinter main loop
        tkinter.mainloop()

#create instance of MyGUI class
if __name__=='__main__':
    my_gui = MyGUI()
