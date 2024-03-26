import numpy as np



def conversion_to_normal(X):
    """
    Converting the data points into log, as we have derived that
    if X ~ f(x, μ, σ^2) then Y ~ N(μ, σ^2) where Y = ln(X)
        - using np.log which convert the list of data into log with base e
    """
    return np.log(X)



# test function
def test_function(X):
    """
    finding out the test function, on which we can 
    say when to reject or accept the null hypothesis.
    """
    n = 100000 
    statistic_values = []
    for i in range(n):
        np.random.seed(i)
        sigma_0 = 13
        mu_0 = 15
        x = np.random.normal(mu_0, sigma_0, 20)
        n = len(x)
        sigma_1 = x.std()
        y = np.exp(-np.sum((x-mu_0)**2)/(2*(sigma_0**2)) + n/2)*(sigma_1/sigma_0)**n
        statistic_values.append(y)

    res = np.sort(statistic_values)
    k = res[round(n*(0.05))]
    if np.exp(-np.sum((X-mu_0)**2)/(2*(13**2)) + n/2)*(sigma_1/sigma_0)**n < k:
        return "Reject the Null hypothesis"
    else:
        return "Accept the Null hypothesis"






if __name__=='__main__':
    print('Question 3:')
    # load the data
    X=np.loadtxt('./DataP1Q3.csv', delimiter=',', skiprows=1)
    Y = conversion_to_normal(X)
    print(test_function(Y))



    


