#Jinny Choe
#5/9/2023
#Week 12 HW Class Exercise 3

#Checkbutton widgets

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        
        #create main window
        self.main_window = tkinter.Tk()
        
        #create 2 frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #3 IntVar objects to use with checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        
        #set the intvar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        
        #create checkbutton widgets in top frame
        self.cb1=tkinter.Checkbutton(self.top_frame,text="Option 1",variable=self.cb_var1)
        self.cb2=tkinter.Checkbutton(self.top_frame,text="Option 2",variable=self.cb_var2)
        self.cb3=tkinter.Checkbutton(self.top_frame,text="Option 3",variable=self.cb_var3)
        
        #pack checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        
        #create OK button & quit button
        self.ok_button = tkinter.Button(self.bottom_frame,text="OK",command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit",command=self.main_window.destroy)
        
        #pack the buttons
        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        #pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #start mainloop
        tkinter.mainloop()
        
    #show_choice method is callback fxn for OK button
    def show_choice(self):
        #create msg string
        self.message = "You selected:\n"
        
        #determine which checkbuttons selected & build msg str accordingly
        if self.cb_var1.get() == 1:
            self.message = self.message +"1\n"
        if self.cb_var2.get() == 1:
            self.message = self.message +"2\n"
        if self.cb_var3.get() == 1:
            self.message = self.message +"3\n"
        
        #display msg in info dialog box
        tkinter.messagebox.showinfo("Select",self.message)
        
#create instance of MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI()