# Importing libraries
import random
import numpy as np
import matplotlib.pyplot as plt


# part (a)


# Algorithm to generate random number from given probability distribution
U = random.uniform(0, 1) ## generating random number from U(0, 1)
F_inv_U = np.sqrt(1/4 - np.log(U)) - 1/2 ## finding F^(-1)(U)
X = F_inv_U
print("Random number generated based on given pdf: ", X)


# Part (b)

# defining the number of sample taken
n = 100000

# Set the seed for reproducibility
random.seed(42)

# Generate 10,0000 random numbers
random_numbers = [random.uniform(0, 1) for _ in range(n)]

# finding the X from given distribution
X = [np.sqrt(1/4 - np.log(U)) - 1/2 for U in random_numbers]

# estimated expected value is given by average of this X
print("Estimated Expected value using monte carlo technique: ", np.average(X))


# part (c)

def pdf(x):
    return (2*x+1)*np.exp(-x*x-x)

# set the same seed as part (b)
random.seed(42)

# Generate 10,000 random numbers
random_nums = [random.uniform(0, 1) for _ in range(10000)]

# generating random numbers from pdf
X = [np.sqrt(1/4 - np.log(U)) - 1/2 for U in random_nums]

plt.hist(X, bins=50, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')

# Generate x values for the probability density function
x_values = np.linspace(0, 3, 1000)

# Plot the probability density function
plt.plot(x_values, pdf(x_values), color='red', label='PDF: (2x+1)e^(-x^2-x)')
# Add labels and legend
plt.title('Histogram with Probability Density Function')
plt.xlabel('Value')
plt.ylabel('Density/Probability')
plt.legend()
plt.grid(True)
plt.show()


# part (d)

# defining cdf for given pdf 
def cdf(x):
    return 1 - np.exp(-x**2 - x)

# defining empirical function
def emp_fun(X, x):
    X_sorted = np.sort(X)
    n = len(X)
    k_values = []
    for val in x:
        k = np.sum(X_sorted < val)
        k_values.append(k)
    return np.array(k_values) / n

# Plotting the empirical function 
plt.plot(np.linspace(0, 3, 3000), emp_fun(X, np.linspace(0, 3, 3000)), marker='.', linestyle='-', color='blue', label='Empirical Distribution Function')

# Plotting the function 1 - e^(-x^2 - x)
plt.plot(np.linspace(0, 3, 3000), cdf(np.linspace(0, 3, 3000)), color='red', label='$1 - e^{-x^2 - x}$')

# Adding labels and legend
plt.title('Empirical Distribution Function and $1 - e^{-x^2 - x}$')
plt.xlabel('Values')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)
plt.show()
