#make a digital clock that has big numbers to show the time for easy reading
#import the modules needed (the only tkinter modules we need are tkinter and tkinter.ttk)
#we also need the time module to get the current time


import tkinter as tk
import tkinter.ttk as ttk
import time


#create the main window (the title is "WClock" and the window is 500x160)
clockrt = tk.Tk()
clockrt.title("WClock")
clockrt.geometry("500x160")
clockrt.wm_attributes("-topmost", 1)

#the time will be displayed in a label that fills almost the entire window
#the label is created with the text "00:00" and the font size is the value of the variable "font_size"
#the label is placed in the center of the window
#the label is given a background color of white
#the label is given a foreground color of black
#the label is given a borderwidth of 0
#the label is given a relief of flat
#the colon blinks on or off every second  (depends on whether it was on or off last second)
#the colon is just part of the label's text and is not a separate label

#create label
font_size = 110
label = tk.Label(clockrt, text="00:00", font=("Helvetica", font_size), bg="white", fg="black", borderwidth=0, relief="flat")
label.place(relx=0.5, rely=0.5, anchor="center")


#create the function that draws the label with the time (it has a forever loop that changes the time every second)
def draw_label():
    #if the current second is even, turn the colon on. else, turn it off
    if time.localtime().tm_sec % 2 == 0:
        colon = ":"
    else:
        colon = " "
    #get the current time
    current_time = time.strftime("%I"+colon+"%M %p")
    #set the label's text to the time
    label.config(text=current_time)
    #wait one second
    clockrt.after(1000, draw_label)


#start the main loop
def mainstuff():
    #call the function that draws the label
    draw_label()
    #start the main loop
    clockrt.mainloop()

mainstuff()