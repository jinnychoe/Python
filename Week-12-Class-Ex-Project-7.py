
#Jinny Choe
#5/8/2023
#Week 12 Class Ex Project 8

#two frames
import tkinter

class MyGUI:
    def __init__(self):
        #create main window widget
        self.main_window = tkinter.Tk()

        #create 2 frames, one for top of window, one for bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create 3 label widget for top frame
        self.label1=tkinter.Label(self.top_frame,text='Winken')
        self.label2=tkinter.Label(self.top_frame,text='Blinken')
        self.label3=tkinter.Label(self.top_frame,text='Nod')
        
        #pack labels in top of frame
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        #create 3 label widget for bottom frame
        self.label4=tkinter.Label(self.bottom_frame,text='Winken')
        self.label5=tkinter.Label(self.bottom_frame,text='Blinken')
        self.label6=tkinter.Label(self.bottom_frame,text='Nod')
        
        #pack labels in top of frame
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        #pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

#create instance of MyGUI class
if __name__=='__main__':
    my_gui = MyGUI()