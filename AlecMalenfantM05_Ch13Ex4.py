"""This program will let the user convert celcius to faranheight using a GUI
Alec Malenfant"""
print("Alec Malenfant\n")
import tkinter


class TempConversion:
    def __init__(self):
        #Create the window
        self.main_window = tkinter.Tk()

        #Create the frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

# top fame
        #Create the top labels
        self.c_label = tkinter.Label(self.top_frame, text = "Degrees(C): ")
        self.value1_entry = tkinter.Entry(self.top_frame, width = 10)

        #pack top frame widgets
        self.c_label.pack(side= 'left')
        self.value1_entry.pack(side= 'left')
#mid frame
        #Create the mid labeld
        self.f_label = tkinter.Label(self.mid_frame, text="Degrees(F): ")
            #Create a stringValue()
        self.value2 = tkinter.StringVar()
            #Create label associated with string var
        self.value2_label = tkinter.Label(self.mid_frame, textvariable = self.value2)

        #pack mid frame widgets
        self.f_label.pack(side = 'left')
        self.value2_label.pack(side = 'left')
#bottom frame
        #Create the bottom buttons
        self.conv_button = tkinter.Button(self.bottom_frame, text = "Convert", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)

        #pack bottom frame buttons
        self.conv_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

#all frames
        #pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

#Logic
    #Define logic to convert from C to F
    def convert(self):
        value1 = float(self.value1_entry.get())
        value2 = float(((9/5)*value1)+32)
        self.value2.set(value2)


myConversion = TempConversion()