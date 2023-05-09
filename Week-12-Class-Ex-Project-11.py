#Jinny Choe
#5/9/2023
#Week 12 Class Ex Project 11

import tkinter
import tkinter.messagebox

class KiloConverterGUI: 
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        #create 2 frams to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #create widgets for top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in km: ')
        self.kilo_entry = tkinter.Entry(self.top_frame,width=10)
        
        #pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        #create button widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,text='Convert')
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)
        
        #pack bottom frame's buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
        
    #convert method is callback fxn for calculate button
    def convert(self):
        
        #value entered by user into kilo_entry widget
        kilo = float(self.kilo_entry.get())
        
        #convert km to mi
        miles = kilo*0.6214
        
        #display results in info dialog box
        tkinter.messagebox.showinfo('Results',str(kilo)+' km is equal to '+str(miles)+' mi')

#create instance of KiloConverterGUI class
if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()