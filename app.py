#we will make a program that has widgets that are separated into different programs
#1. a clock (clock.py)
#2. a thermometer (thermometer.py)
#3. a stopwatch (stopwatch.py)
#4. a timer (timer.py)
#5. a calculator (calculator.py)

#widgets should be able to be easily added to the program
#using arrays, this is possible

button_names = ["Clock", "Thermometer (F)", "Thermometer (C)", "Stopwatch", "Timer", "Calculator"]
button_programs = [
    "clock.py",
    "thermometerf.py",
    "thermometerc.py",
    "stopwatch.py",
    "timer.py",
    "calculator.py"
]

#this array will hold the names of the widgets that have been fully programmed
finished_widgets = ["Clock","Thermometer (F)","Thermometer (C)", "Stopwatch","Timer"]

#we need buttons to be able to launch widgets
#this means we need to import tkinter and tkinter.ttk
#we need the time module because we will be using the time.sleep() function
import tkinter as tk
import tkinter.ttk as ttk
import time
import os
#we can use subprocess to launch programs, but we need to make sure that it runs the files from the python3 environment
import subprocess


#create the main window (the title is "WWidgets" and the window is 150x200)
widgetsrt = tk.Tk()
widgetsrt.title("WWidgets")
widgetsrt.geometry("150x200")
#the window stays on top of all other windows
widgetsrt.wm_attributes("-topmost", 1)


#the widgets will be displayed in separate windows
#this is because the widgets are too big to fit in the main window, and because they are meant to be launched from the main window
#create the buttons that will launch the widgets:
def draw_buttons():
    #this function will create the buttons that launch the widgets
    #the buttons will be placed in the top half of the window
    #the buttons will be given a width of 150 and a height of 30
    #the buttons will be given a background color of white
    #the buttons will be given a foreground color of black
    #the buttons will be given a borderwidth of 0
    #the buttons will be given a relief of raised

    #create the buttons
    for i in range(len(finished_widgets)):
        #create the button
        button = tk.Button(widgetsrt, text=button_names[i], bg="white", fg="black", borderwidth=4, relief="raised")
        #place the button
        button.place(relx=0.5, rely=0.5+i*0.1, anchor="center")
        #bind the button to the function that launches the widget
        button.bind("<Button-1>", lambda event, i=i: launch_widget(i))


#create the function that launches the widget
def launch_widget(i):
    #this function will launch the widget
    #the widget will be launched by calling the program that is in the array "button_programs"
    #the widget will be launched with the subprocess module
    #we will use the command "python3 ./program.py"
    #first, we cd into the directory that contains the program, which is the same directory that contains this file
    #however, most terminals default to a directory that is not the same as the directory that contains this file
    #so we need to cd into the directory that contains this file
    #we will use the os module to do this
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #now we can launch the program
    subprocess.Popen(["python3", "./"+button_programs[i]])


#start the main loop
def main():
    #call the function that draws the buttons
    draw_buttons()
    #start the main loop
    widgetsrt.mainloop()

main()