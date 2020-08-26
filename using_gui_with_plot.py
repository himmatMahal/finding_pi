import tkinter as tk
import matplotlib.pyplot as plt
import math

class VisualizingPi:
    # initialize the main window:
    def __init__(self, master):
        self.master = master

        self.HEIGHT = 600
        self.WIDTH = 800
        self.RADIOBUTTON_FONT = ("Helvetica", 14, "bold")

        self.button_start_var = tk.IntVar()
        self.button_end_var = tk.IntVar()

        self.start_buttons = [None]*5
        self.starting_options = [0,1,10,100,1000]
        self.end_buttons = [None]*5
        self.ending_options = [5,10,25,500,5000]

        master.title('Visualizing Pi')
        self.canvas = tk.Canvas(master, height=self.HEIGHT, width=self.WIDTH, bg='#2c2c4d')
        self.canvas.pack()

        # two loops below create 5 radio buttons each
        i=0
        for button in self.end_buttons:
            button = tk.Radiobutton(self.canvas, text='{}'.format(self.ending_options[i]), variable=self.button_end_var,
                            value=self.ending_options[i], command=self.set_end, bg='#2c2c4d',fg='white',
                            font=self.RADIOBUTTON_FONT, selectcolor='red')
            self.end_buttons[i] = button
            y_position = float(i/9) + 0.1
            button.place(relx=0.3,rely=y_position)
            i=i+1
        i=0
        for button in self.start_buttons:
            button = tk.Radiobutton(self.canvas, text='{}'.format(self.starting_options[i]), variable=self.button_start_var,
                            value=self.starting_options[i], command=self.set_start, bg='#2c2c4d',fg='white',
                            font=self.RADIOBUTTON_FONT, selectcolor='red')
            self.start_buttons[i] = button
            y_position = float(i/9) + 0.1
            button.place(relx=0.1,rely=y_position)
            i=i+1

    # functions to set starting and ending points:
    def set_start(self):
        print("{} was selected (start)".format(self.button_start_var.get()))

    def set_end(self):
        print("{} was selected (end)".format(self.button_end_var.get()))
        i=0
        for x in self.starting_options:
            if self.button_end_var.get() <= x:
                self.start_buttons[i].configure(state='disabled')
                if self.button_start_var.get()>=self.button_end_var.get():
                    self.start_buttons[0].select()
            else:
                self.start_buttons[i].configure(state='normal')
            i=i+1


def main():
    root_window = tk.Tk()
    run_app = VisualizingPi(root_window)
    root_window.mainloop()

if __name__ == '__main__':
    main()
