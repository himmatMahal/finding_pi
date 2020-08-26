import matplotlib.pyplot as plt
import math

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

def leibniz_madhava(terms=10):
    # https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    pi_sum = 0.0
    for i in range(1, terms):
        n = (2*i - 1)*((-1)**(i+1))
        pi_sum += 1/n
    pi_approx = 4*pi_sum
    return pi_approx

def odd_product_formula(terms=10):
    # https://en.wikipedia.org/wiki/List_of_formulae_involving_%CF%80 - under 'other infinite series'
    pi_sum = 0.00
    for i in range(terms):
        n = ((4*i)+1)*((4*i)+3)
        pi_sum += 1/n
    pi_approx = 8*pi_sum
    return pi_approx

ending_point = int(input("Enter the number of terms at which to stop the formulas at: "))
starting_point = int(input("Enter the number of terms to start comparing formulas: "))

# creating lists of approximations of pi based on starting and ending points
difference = ending_point-starting_point
step = 2 * int( (ending_point-starting_point) / 100) + 1
y_axis_pts_all = range(starting_point, ending_point)
# leibniz_madhava formula needs an odd step, otherwise, graph bounces erratically up and down
# very fast

if(starting_point <= ending_point and difference<10000):
    # difference cannot be too big, otherwise computer has hard time loading plot
    y_axis_pts_listtwo = range(starting_point, ending_point, step)
    list_two = [leibniz_madhava(x) for x in range(starting_point, ending_point, step)]
    list_one = [odd_product_formula(x) for x in range(starting_point, ending_point)]
    list_three = [wallis(x) for x in range(starting_point, ending_point)]
    list_four = [basel(x) for x in range(starting_point, ending_point)]
    pi_constant = [math.pi for x in range(starting_point, ending_point)]

    # creating a graphical plot of each formula
    plt.plot(y_axis_pts_all, pi_constant, linestyle='--', label = 'Real value of pi')
    plt.plot(y_axis_pts_all, list_one, label = 'odd product formula')
    plt.plot(y_axis_pts_listtwo, list_two, label = 'leibniz-madhava', linestyle = '-')
    plt.plot(y_axis_pts_all, list_three, label = 'Wallis product')
    plt.plot(y_axis_pts_all, list_four, label = 'Basel formula')

    plt.xlabel('Number of terms in function')
    plt.legend()
    plt.show()

else:
    plt.title('Starting point must be greater than ending point,\n and the maximum difference is 9999. Please try again:')
    plt.show()
