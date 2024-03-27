import numpy as np



def conversion_to_normal(X):
    """
    Converting the data points into log, as we have derived that
    if X ~ f(x, μ, σ^2) then Y ~ N(μ, σ^2) where Y = ln(X)
        - using np.log which convert the list of data into log with base e
    """
    return np.log(X)


def generate_normal_random_numbers(mu, sigma, nums):
    u1 = np.random.rand(nums)
    u2 = np.random.rand(nums)
    # Box-Muller transform
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
    # Scale and shift to get desired mean and standard deviation
    z1 = z1 * sigma + mu
    return z1



# test function
def test_function(X):
    """
    finding out the test function, on which we can 
    say when to reject or accept the null hypothesis.
    """
    n = 100000 
    statistic_values = []
    for i in range(n):
        sigma_0 = 13
        mu_0 = 15
        x = generate_normal_random_numbers(mu_0, sigma_0, 20)
        n = len(x)
        sigma_1 = x.std()
        y = np.exp(-np.sum((x-mu_0)**2)/(2*(sigma_0**2)))*(sigma_1)**n
        statistic_values.append(y)

    res = np.sort(statistic_values)
    k = res[round(n*(0.05))]
    if np.exp(-np.sum((X-mu_0)**2)/(2*(sigma_0**2)))*(sigma_1)**n < k:
        return "Reject the Null hypothesis"
    else:
        return "Accept the Null hypothesis"





if __name__=='__main__':
    print('Question 3:')
    # load the data
    X=np.loadtxt('./DataP1Q3.csv', delimiter=',', skiprows=1)
    Y = conversion_to_normal(X)
    print(test_function(Y))
