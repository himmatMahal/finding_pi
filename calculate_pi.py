

# Below are a few functions that calculate pi
def basel(iterations=10):
    # https://en.wikipedia.org/wiki/Basel_problem
    pi_sum = 0.0
    for i in range(1, iterations+1):
        pi_sum = pi_sum + (i**(-2))

    pi_approx = (6*pi_sum)**(0.5)
    print("{} iterations using Eulers infinite series yields: {}".format(i, pi_approx))

def wallis(iterations=10):
    # https://en.wikipedia.org/wiki/Wallis_product
    pi_prod = 1.0
    for i in range(1, iterations+1):
        n = float(i)
        pi_prod = pi_prod*( ((2*n)**2) /( ((2*n)-1)*((2*n)+1) ) )

    pi_approx = 2*pi_prod
    print("{} iterations using Wallis product yields: {}".format(i, pi_approx))

def leibniz_madhava(iterations=10):
    # https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    pi_sum = 0.0
    for i in range(1, iterations+1):
        n = (2*i - 1)*((-1)**(i+1))
        pi_sum = pi_sum + 1/n

    pi_approx = 4*pi_sum
    print("{} iterations using Leibniz-Madhava formula yields: {}".format(i, pi_approx))


basel(10000)
wallis(10000)
leibniz_madhava(10000)
