#make a stopwatch with second and millisecond counters
#import the modules needed (the only tkinter modules we need are tkinter and tkinter.ttk)
#there is a button that starts/stops the stopwatch
#the stopwatch label is formatted with .format() and is updated every second
#it is in hh:mm:ss.ms format


import tkinter as tk
import tkinter.ttk as ttk

#import time so that we can use time.time()
import time


#set up the main window
swroot = tk.Tk()
swroot.title("WStopwatch")
swroot.geometry("350x150")
swroot.wm_attributes("-topmost", 1)


#set up the label that will show the time
font_size = 60
swlabel = tk.Label(swroot, font=("Helvetica", font_size), text="00:00:00.0")
swlabel.pack(pady=10)



#create a function to start/stop the stopwatch
def start_stopwatch():
    global swrunning
    if swrunning:
        #stop the stopwatch
        swrunning = False
        swbutton.config(text="Start")
    else:
        
        #start the stopwatch
        swrunning = True
        global swstart
        swstart = time.time()
        swbutton.config(text="Stop")
        swbutton.after(1, update_stopwatch)

#set up the button
swbutton = ttk.Button(swroot, text="Start", command=start_stopwatch)
swbutton.pack(pady=10)

#create a function to update the stopwatch
def update_stopwatch():
    if swrunning:
        #update the time
        swtime = time.time() - swstart
        swlabel.config(text=str(int(swtime/3600%24)).zfill(2) + ":" + str(int(swtime/60%60)).zfill(2) + ":" + str(int(swtime)).zfill(2) + "." + str(int((swtime%1)*10)).zfill(1))
        swbutton.after(1, update_stopwatch)
    


#start the stopwatch
swrunning = False
swbutton.config(text="Start")
swbutton.after(1, update_stopwatch)


#start the main loop
swroot.mainloop()


#end of program