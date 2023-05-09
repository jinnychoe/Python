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
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        #create widgets for top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in km: ')
        self.kilo_entry = tkinter.Entry(self.top_frame,width=10)
        
        #pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        #widgets for middle frame
        self.descr_label = tkinter.Label(self.mid_frame,text='Converted to miles: ')
        
        #initialize StrVar obejct for output label
        self.value = tkinter.StringVar()
        
        #StrVar object to associate with output label
        #Value in StrVar will be displayed in label
        self.miles_label = tkinter.Label(self.mid_frame,textvariable=self.value)
        
        #pack middle frame widget
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')
        
        #create button widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,text='Convert')
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)
        
        #pack bottom frame's buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
        
    #convert method is callback fxn for calculate button
    def convert(self):
        
        #value entered by user into kilo_entry widget
        kilo = float(self.kilo_entry.get())
        
        #convert km to mi
        miles = kilo*0.6214
        
        #convert mi to str & store in StrVar object
        #will automatically update miles_label widget
        self.value.set(miles)
        
#create instance of KiloConverterGUI class
if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()