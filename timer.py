#make a timer that counts down from an inputted time
#import the modules needed (the only tkinter modules we need are tkinter and tkinter.ttk)
#there is a button that starts/stops the timer


import tkinter as tk
import tkinter.ttk as ttk


#import time so that we can use time.time()
import time


#set up the main window
troot = tk.Tk()
troot.title("WTimer")
troot.geometry("350x150")
troot.wm_attributes("-topmost", 1)


#set up the label that will show the time left
font_size = 60
tlabel = tk.Label(troot, font=("Helvetica", font_size), text="0 seconds")
tlabel.pack(pady=10)


global trunning
trunning = False

#create the input box
font_size_input = 20
tinput = tk.Entry(troot, font=("Helvetica", font_size_input))
tinput.pack(pady=10)


#set up the function that will be called when the button is pressed
def start_timer():
    global trunning
    if trunning:
        trunning = False
        tbutton.config(text="Start")
    else:
        trunning = True
        tbutton.config(text="Stop")
        start_time = time.time()
        time_left = int(tinput.get())
        originalinput = int(tinput.get())
        while time_left > 0 and trunning:
            time_left = originalinput - int(time.time() - start_time)
            tlabel.config(text=str(time_left) + " seconds")
            troot.update()
            time.sleep(0.1)
        tlabel.config(text="0 seconds")
        troot.update()
        trunning = False
        tbutton.config(text="Start")


#set up the button (it will be at the top left of the window)
tbutton = ttk.Button(troot, text="Start", command=start_timer)
tbutton.pack(pady=10)
#set position of the button
tbutton.place(relx=0.5, rely=0.5, anchor="n")


#start the main loop
troot.mainloop()