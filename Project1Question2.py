import numpy as np
from matplotlib import pyplot as plt

# Question 2(a)
# since we can not get a closed form of MLE so we have to use numerical method to find the MLE
# we use the gradient descent method to find the MLE

def optimise_theta(theta,xi,alpha): #gradient descent method
    """
    This function takes the initial value of theta, the data xi and the learning rate alpha as input and returns 
    the optimal value of theta and array of thetas at each iteration"""
    n=len(xi)
    thetas=[theta]
    for _ in range(1000):
        sum_xi=xi.sum()
        exp_xi_by_theta=np.exp(-xi/theta)
        one_minus_exp_xi_by_theta=1-exp_xi_by_theta
        term=(xi*exp_xi_by_theta)/one_minus_exp_xi_by_theta
        grad=(n*theta-sum_xi+term.sum())/theta**2
        theta=theta-alpha*grad
        thetas.append(theta)
    return theta,thetas

#Question 2(b)
def generate_random_data(theta,n,seed):
    """
    This function takes the value of theta, the number of random numbers to be generated and the seed as input and returns
    n random numbers generated from the given distribution with the given theta and seed.
    """
    np.random.seed(seed) # set the seed
    u=np.random.rand(n) #generates n random numbers between 0 and 1
    return -theta*np.log(1-np.sqrt(u)) 
    
def get_estimated_mles(theta,num_estimates,alpha):
    """
    theta: the true value of theta
    num_estimates: number of estimates to be made
    alpha: the learning rate
    """
    estimated_mles=[]
    for i in range(num_estimates):
        xi=generate_random_data(theta,100,seed=i) #generate random data
        estimated_mle,thetas=optimise_theta(theta+1,xi,alpha) #get the estimated mle for the generated data and iteration number is used as seed
        estimated_mles.append(estimated_mle)
    ans=np.array(estimated_mles)
    return ans

def get_mse_bias(estimated_mles,theta):
    """
    This function takes the estimated mles and the true value of theta as input and returns the mean squared error and the bias
    """
    mse=np.mean((estimated_mles-theta)**2)
    bias=np.mean(estimated_mles-theta)
    return mse,bias


if __name__=='__main__':
    print('Question 2(a)')
    # load the data
    xi=np.loadtxt('./DataP1Q2.csv',delimiter=',')
    #initialize the parameters
    theta=1
    alpha=0.001 # learning rate
    # estimate the MLE
    theta,thetas=optimise_theta(theta,xi,alpha)
    print('The MLE of theta is:',theta)
    plt.plot(np.linspace(0,1000,1001),thetas)
    plt.xlabel('Iteration')
    plt.ylabel('Theta')
    plt.show()
    print('Question 2(b)')
    actual_thetas=[0.5,1,2]
    for theta in actual_thetas:
        estimated_mles=get_estimated_mles(theta,100,0.001)
        mse,bias=get_mse_bias(estimated_mles,theta)
        print(f"theta={theta}, mse={mse}, bias={bias}")


