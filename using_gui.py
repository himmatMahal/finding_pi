import tkinter as tk
import matplotlib.pyplot as plt
import math

HEIGHT = 600
WIDTH = 800
RADIOBUTTON_FONT = ("Helvetica", 14, "bold")

# NOTE: make application object oriented once complete:
# https://docs.python.org/2/library/tkinter.html#a-simple-hello-world-program

def create_plots():
    plt.show()
# put plotted graphs on screen

def clear_plots():
    return
# remove all plots

def set_start():
    print("{} was selected (start)".format(button_start_var.get()))

def set_end():
    print("{} was selected (end)".format(button_end_var.get()))
    i=0
    for x in starting_options:
        if button_end_var.get() <= x:
            start_buttons[i].configure(state='disabled')
            if button_start_var.get()>button_end_var.get():
                start_buttons[0].select()
        else:
            start_buttons[i].configure(state='normal')
        i=i+1
    # for purposes of this application, starting point must be
    # less than ending point.if/else statement above makes it impossible
    # for the starting point to be greater than the ending point


# configure starting and ending points of graph

screen = tk.Tk()
screen.title('Finding Pi')

canvas = tk.Canvas(screen, height=HEIGHT, width=WIDTH, bg='#2c2c4d')
canvas.pack()
# putting a canvas on the window to put other widgets on

button_start_var = tk.IntVar()

start_buttons = [None]*5
starting_options = [0,1,10,100,1000]
i=0
for button in start_buttons:
    button = tk.Radiobutton(canvas, text='{}'.format(starting_options[i]), variable=button_start_var,
                    value=starting_options[i], command=set_start, bg='#2c2c4d',
                    fg='white', font=RADIOBUTTON_FONT, selectcolor='red')
    y_position = float(i/9) + 0.1
    start_buttons[i] = button
    button.place(relx=0.1,rely=y_position)
    i=i+1
# code above creates an empty list, and fills it with 5 radiobutton objects
# then places the 5 starting point radiobuttons on the canvas

button_end_var = tk.IntVar()

end_buttons = [None]*5
ending_options = [5,10,25,500,5000]
i=0
for button in end_buttons:
    button = tk.Radiobutton(canvas, text='{}'.format(ending_options[i]), variable=button_end_var,
                    value=ending_options[i], command=set_end, bg='#2c2c4d',fg='white',
                    font=RADIOBUTTON_FONT, selectcolor='red')
    end_buttons[i] = button
    y_position = float(i/9) + 0.1
    button.place(relx=0.3,rely=y_position)
    i=i+1
# making radio buttons to select ending points








# Making sure that the starting point is less than the end point by disabling starting
# radiobuttons greater than the selected ending point button

screen.mainloop()
