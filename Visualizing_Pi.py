import tkinter as tk
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import numpy as nmp
import os.path

# Below are a few functions that calculate pi
def basel(terms=10):
    # https://en.wikipedia.org/wiki/Basel_problem
    pi_sum = nmp.longdouble(0.0)
    for i in range(1, terms):
        pi_sum += (i**(-2))
    pi_approx = nmp.longdouble((6*pi_sum)**(0.5))
    return pi_approx
def wallis(terms=10):
    # https://en.wikipedia.org/wiki/Wallis_product
    pi_product = nmp.longdouble(1.0)
    for i in range(1, terms):
        n = float(i)
        pi_product = pi_product*( ((2*n)**2) /( ((2*n)-1)*((2*n)+1) ) )
    pi_approx = nmp.longdouble(2*pi_product)
    return pi_approx
def odd_product_formula(terms=10):
    # https://en.wikipedia.org/wiki/List_of_formulae_involving_%CF%80 - under 'other infinite series'
    pi_sum = nmp.longdouble(0.0)
    for i in range(terms):
        n = ((4*i)+1)*((4*i)+3)
        pi_sum += 1/n
    pi_approx = nmp.longdouble(8*pi_sum)
    return pi_approx
def leibniz_madhava(terms=10):
    # https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    pi_sum = nmp.longdouble(0.0)
    for i in range(1, terms):
        n = (2*i - 1)*((-1)**(i+1))
        pi_sum += 1/n
    pi_approx = nmp.longdouble(4*pi_sum)
    return pi_approx

class VisualizingPi:
    """
    Class represents a GUI object with buttons, and various options to create graphs
    that show how various infinite series which calculate Pi behave
    """
    def __init__(self, master):
        """
        Construct functioning GUI attributes like buttons, labels, etc.
        """
        self.master = master
        self.HEIGHT = 600
        self.WIDTH = 600
        self.RADIOBUTTON_FONT = ("Helvetica", 11, "bold")
        self.LABEL_FONT = ("Helvetica", 12, "bold")
        self.graph_buttons = [None]*4
        self.start_buttons = [None]*6
        self.end_buttons = [None]*6
        # lists above create empty lists, which will be filled with button objects below
        self.starting_options = [0,1,10,100,1000,3000]
        self.ending_options = [10,50,500,2500,5000,10000]
        self.graph_button_text = ['Basel','Wallis','Leibniz-Madhava','Sum of Odd\nProducts']
        self.button_start_var = tk.IntVar()
        self.button_end_var = tk.IntVar(value=self.ending_options[-1])
        # by default, start is 0 and end is maximum possible value
        self.options_selected = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
        # list above keeps track of which buttons are toggled (0 - off, 1 - on)

        master.title('Visualizing Pi')
        self.canvas = tk.Canvas(master, height=self.HEIGHT, width=self.WIDTH, bg='#ccc5b9')
        self.canvas.pack()

        # inserting image legend that describes each formula, if image isnt found, display error message
        if os.path.isfile("legend.PNG"):
            self.legend_img = ImageTk.PhotoImage(Image.open("legend.PNG").resize((473,230), Image.ANTIALIAS))
            self.image_panel = tk.Label(self.canvas, image = self.legend_img)
            self.image_panel.place(relx=0.1,rely=0.55)
        else:
            self.image_error_label = tk.Label(self.canvas,
                            text='ERROR: Image not found\nPlease keep legend.PNG in the same directory as this program\n',
                            font = self.LABEL_FONT, justify='left', bg='#ccc5b9')
            self.image_error_label.place(relx=0.1,rely=0.55)

        # two loops below create 5 radio buttons each
        i=0
        self.radiobtn_label = tk.Label(self.canvas, text='Select a starting and ending\npoint for your graph(s):',
                        font = self.LABEL_FONT, justify='left', bg='#ccc5b9')
        self.radiobtn_label.place(relx=0.1,rely=0.065)
        for button in self.end_buttons:
            button = tk.Radiobutton(self.canvas, text='{}'.format(self.ending_options[i]), variable=self.button_end_var,
                            value=self.ending_options[i], command=self.check_start_end, bg='#ccc5b9',fg='#403d39',
                            font=self.RADIOBUTTON_FONT, selectcolor='#eb5e28')
            self.end_buttons[i] = button
            y_position = float(i/15) + 0.15
            button.place(relx=0.3,rely=y_position)
            i=i+1
        i=0
        for button in self.start_buttons:
            button = tk.Radiobutton(self.canvas, text='{}'.format(self.starting_options[i]), variable=self.button_start_var,
                            value=self.starting_options[i], bg='#ccc5b9',fg='#403d39',
                            font=self.RADIOBUTTON_FONT, selectcolor='#eb5e28')
            self.start_buttons[i] = button
            y_position = float(i/15) + 0.15
            button.place(relx=0.1,rely=y_position)
            i=i+1

        # adding button to toggle plots
        self.show_plots = tk.Button(self.canvas, text='Create\nGraphs', bg='#eb5e28',
                    fg='#252422', command=self.create_plots, font=self.LABEL_FONT, justify='left')
        self.show_plots.place(relx=0.5, rely=0.429, relwidth=0.14, relheight=0.09)

        # adding button to toggle accuracy plot
        self.show_accuracy_plot = tk.Button(self.canvas, text='Plot\nAccuracy', bg='#eb5e28',
                    fg='#252422', command=self.create_accuracy_plot, font=self.LABEL_FONT, justify='left')
        self.show_accuracy_plot.place(relx=0.67, rely=0.429, relwidth=0.14, relheight=0.09)

        # loop to create checkbuttons to give user options of which graphs to add
        i=0
        self.graphbtn_label = tk.Label(self.canvas, text='Select which graphs you would\nlike to display:',
                        font = self.LABEL_FONT, justify='left', bg='#ccc5b9')
        self.graphbtn_label.place(relx=0.5,rely=0.065)
        for button in self.graph_buttons:
            button = tk.Checkbutton(self.canvas, text = '{}'.format(self.graph_button_text[i]), variable = self.options_selected[i],
                                    bg='#ccc5b9',fg='#403d39', font=self.RADIOBUTTON_FONT, selectcolor='#eb5e28')
            y_position = float(i/15) + 0.15
            button.place(relx=0.5,rely=y_position)
            i=i+1

    def check_start_end(self):
        """
        Disable all starting option radiobuttons which are less than the selected
        ending option
        """
        i=0
        for x in self.starting_options:
            if self.button_end_var.get() <= x:
                self.start_buttons[i].configure(state='disabled')
                if self.button_start_var.get()>=self.button_end_var.get():
                    self.start_buttons[0].select()
            else:
                self.start_buttons[i].configure(state='normal')
            i=i+1

    def create_plots(self):
        """
        Create plots based on which starting/ending points and which
        pi-approximating functions were selected
        """
        x_values = nmp.array(range(self.button_start_var.get(), self.button_end_var.get()))
        # the 'step' below ensures that the list of points will not be too long
        # to help graphs load faster
        step = 2 * int( nmp.size(x_values) / 100) + 1
        x_values = x_values[::step]
        plt.style.use('Solarize_Light2')
        plt.plot([x_values[0],x_values[-1]], [nmp.pi, nmp.pi], linestyle='-.', label='Actual value of PI (16 s.f)')
        plt.annotate('PI: {}'.format(nmp.pi),(x_values[0], nmp.pi),
                    bbox=dict(boxstyle="round,pad=0.25"), fontsize=9)
        plt.xlabel('Number of terms used to approximate Pi')
        plt.ylabel('Approximated value of Pi')
        if self.options_selected[0].get()==1:
            plt.plot(x_values, nmp.array([basel(x) for x in x_values]),
                    label='Basel:\n{}'.format(basel(x_values[-1])), linewidth=1)
        if self.options_selected[1].get()==1:
            plt.plot(x_values, nmp.array([wallis(x) for x in x_values]),
                    label='Wallis:\n{}'.format(wallis(x_values[-1])), linewidth=1)
        if self.options_selected[2].get()==1:
            y_values = [leibniz_madhava(x) for x in x_values]
            plt.plot(x_values, nmp.array([leibniz_madhava(x) for x in x_values]),
                    label='Leibniz-Madhava:\n{}'.format(leibniz_madhava(x_values[-1])), linewidth=1)
        if self.options_selected[3].get()==1:
            plt.plot(x_values, nmp.array([odd_product_formula(x) for x in x_values]),
                    label='Sum of Odd Products:\n{}'.format(odd_product_formula(x_values[-1])), linewidth=1)
        # control statements below change y-axis zoom based on start/end points
        # to give it a cleaner look
        if self.button_end_var.get() > 500:
            plt.ylim(3.140,3.143)
        elif self.button_end_var.get() > 50:
            plt.ylim(3.11,3.17)
        elif self.button_end_var.get() > 10:
            plt.ylim(3,3.3)
        plt.title('Approximating Pi using infinite series')
        plt.legend(loc=1, fontsize=7)
        plt.show()

    def create_accuracy_plot(self):
        """
        Create a bar graph that displays each pi-approximating functions percent accuracy
        """
        accuracy_list = []
        name_list = []
        colors = []
        if self.options_selected[0].get()==1:
            accuracy_list.append( nmp.longdouble(100) * basel(self.button_end_var.get())/nmp.pi )
            name_list.append(self.graph_button_text[0])
            colors.append('#ffcdb2')
        if self.options_selected[1].get()==1:
            accuracy_list.append( nmp.longdouble(100) * wallis(self.button_end_var.get())/nmp.pi )
            name_list.append(self.graph_button_text[1])
            colors.append('#e5989b')
        if self.options_selected[2].get()==1:
            accuracy_list.append( nmp.longdouble(100) * leibniz_madhava(self.button_end_var.get()-1)/nmp.pi )
            name_list.append(self.graph_button_text[2])
            colors.append('#ffb4a2')
        if self.options_selected[3].get()==1:
            accuracy_list.append( nmp.longdouble(100) * odd_product_formula(self.button_end_var.get())/nmp.pi )
            name_list.append(self.graph_button_text[3])
            colors.append('#b5838d')
        plt.style.use('Solarize_Light2')
        plt.bar(name_list,accuracy_list,color=colors)
        i=0
        for percent in accuracy_list:
            plt.annotate('{}%'.format(percent),(i,percent),
                         bbox=dict(boxstyle="round,pad=0.25", facecolor='#ffe5d9'), fontsize=6)
            i=i+1
        plt.xlabel('Approximation formula used')
        plt.ylabel('Percent accuracy')
        # control statements below change y-axis zoom based on start/end points
        # to give it a cleaner look
        if self.button_end_var.get() < 500:
            plt.ylim(95,100)
        elif self.button_end_var.get() < 5000:
            plt.ylim(99.9,100)
        else:
            plt.ylim(99.99,100)
        plt.title('Percent accuracy of each formula used\n')
        plt.show()


def main():
    root_window = tk.Tk()
    run_app = VisualizingPi(root_window)
    root_window.mainloop()

if __name__ == '__main__':
    main()
