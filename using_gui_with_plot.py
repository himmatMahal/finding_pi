import tkinter as tk
import matplotlib.pyplot as plt
import math
import numpy as nmp

# Below are a few functions that calculate pi
def basel(terms=10):
    # https://en.wikipedia.org/wiki/Basel_problem
    pi_sum = 0.0
    for i in range(1, terms):
        pi_sum += (i**(-2))
    pi_approx = (6*pi_sum)**(0.5)
    return pi_approx

def wallis(terms=10):
    # https://en.wikipedia.org/wiki/Wallis_product
    pi_product = 1.0
    for i in range(1, terms):
        n = float(i)
        pi_product = pi_product*( ((2*n)**2) /( ((2*n)-1)*((2*n)+1) ) )
    pi_approx = 2*pi_product
    return pi_approx

def odd_product_formula(terms=10):
    # https://en.wikipedia.org/wiki/List_of_formulae_involving_%CF%80 - under 'other infinite series'
    pi_sum = 0.00
    for i in range(terms):
        n = ((4*i)+1)*((4*i)+3)
        pi_sum += 1/n
    pi_approx = 8*pi_sum
    return pi_approx

def leibniz_madhava(terms=10):
    # https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    pi_sum = 0.0
    for i in range(1, terms):
        n = (2*i - 1)*((-1)**(i+1))
        pi_sum += 1/n
    pi_approx = 4*pi_sum
    return pi_approx

class VisualizingPi:
    # initialize the main window:
    def __init__(self, master):
        self.master = master

        self.HEIGHT = 600
        self.WIDTH = 800
        self.RADIOBUTTON_FONT = ("Helvetica", 14, "bold")
        self.LABEL_FONT = ("Helvetica", 12,)

        self.graph_buttons = [None]*4
        self.start_buttons = [None]*5
        self.end_buttons = [None]*5
        # lists above create empty lists, which will be filled with button objects below

        self.starting_options = nmp.array([0,1,10,100,1000])
        self.ending_options = nmp.array([5,10,25,500,5000])
        self.graph_button_text = ['Basel','Wallis','Leibniz-Madhava','Sum of Odd Products']

        # Later on, use latex to style font:
        # https://matplotlib.org/3.1.1/tutorials/text/usetex.html

        self.button_start_var = tk.IntVar()
        # by default, start is 0 and end is maximum possible value
        self.button_end_var = tk.IntVar(value=self.ending_options[-1])

        # list below keeps track of which buttons are toggled (0 - off, 1 - on)
        self.options_selected = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]

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

        # adding labels to display current selected points
        self.start_label = tk.Label(self.canvas, text='Starting \npoint \nselected: {}'.format(self.button_start_var.get()),
                                    font = self.LABEL_FONT)
        self.end_label = tk.Label(self.canvas, text='Ending \npoint \nselected: {}'.format(self.button_end_var.get()),
                                    font = self.LABEL_FONT)
        self.start_label.place(relx=0.1, rely=0.7, relwidth=0.14, relheight=0.12)
        self.end_label.place(relx=0.3, rely=0.7, relwidth=0.14, relheight=0.12)

        # adding buttons to toggle plots
        self.show_plots = tk.Button(self.canvas, text='show plots', command=self.create_plots)
        self.show_plots.place(relx=0.1, rely=0.85, relwidth = 0.34)

        # loop to create checkbuttons to give user options of which graphs to add
        i=0
        for button in self.graph_buttons:
            button = tk.Checkbutton(self.canvas, text = '{}'.format(self.graph_button_text[i]), variable = self.options_selected[i],
                                    bg='#2c2c4d',fg='white', font=self.RADIOBUTTON_FONT, selectcolor='red')
            y_position = float(i/9) + 0.1
            button.place(relx=0.55,rely=y_position)
            i=i+1


    # methods to set starting and ending points, will be used when radio buttons are clicked:
    def set_start(self):
        self.start_label.configure(text='Starting \npoint \nselected: {}'.format(self.button_start_var.get()))
    def set_end(self):
        self.end_label.configure(text='Ending \npoint \nselected: {}'.format(self.button_end_var.get()))
        i=0
        for x in self.starting_options:
            if self.button_end_var.get() <= x:
                self.start_buttons[i].configure(state='disabled')
                if self.button_start_var.get()>=self.button_end_var.get():
                    self.start_buttons[0].select()
                    self.start_label.configure(text='Ending \npoint \nselected: {}'.format(self.button_start_var.get()))
            else:
                self.start_buttons[i].configure(state='normal')
            i=i+1

    # method(s) to create graphs
    def create_plots(self):
        x_values = range(self.button_start_var.get(), self.button_end_var.get())
        plt.plot(x_values, [nmp.pi for x in x_values])
        if self.options_selected[0].get()==1:
            plt.plot(x_values, [basel(x) for x in x_values])
        if self.options_selected[1].get()==1:
            plt.plot(x_values, [wallis(x) for x in x_values])
        if self.options_selected[2].get()==1:
            step = 2 * int( nmp.size(x_values) / 100) + 1
            x_values = x_values[::step]
            y_values = [leibniz_madhava(x) for x in x_values]
            # this formula bounces up and down, to make it look neater,
            # a step is introduced, so it bounces up and down less aggresively
            plt.plot(x_values, [leibniz_madhava(x) for x in x_values])
        if self.options_selected[3].get()==1:
            plt.plot(x_values, [odd_product_formula(x) for x in x_values])
        plt.show()

def main():
    root_window = tk.Tk()
    run_app = VisualizingPi(root_window)
    root_window.mainloop()

if __name__ == '__main__':
    main()
