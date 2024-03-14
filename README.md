# Statistical Inference Project 1
## Question 2(a)
```math
    \begin{align*}
        & F(x)=\begin{cases}
            \left(1-e^{-\frac{x}{\theta}}\right)^2 & x> 0\\
            0 & x\leq0\\
            \end{cases}\\
    \end{align*}
```
in the given data set DataP1Q2.csv, we have 53 data points and we want to estimate $ \theta $ using MLE. The likelihood function is defined in terms of PDF so we have to differentiate the given CDF :
```math
    \begin{align*}
        & f(x|\theta)=\frac{d}{dx}F(x|\theta)\\
        & f(x|\theta)=\frac{d}{dx}\left(1-e^{-\frac{x}{\theta}}\right)^2\\
        & f(x|\theta)=2\left(1-e^{-\frac{x}{\theta}}\right)\frac{d}{dx}\left(1-e^{-\frac{x}{\theta}}\right)\\
        & f(x|\theta)=2\left(1-e^{-\frac{x}{\theta}}\right)\left(\frac{1}{\theta}e^{-\frac{x}{\theta}}\right)\\
        & f(x|\theta)=\frac{2}{\theta}\left(1-e^{-\frac{x}{\theta}}\right)e^{-\frac{x}{\theta}}\\
    \end{align*}
```
Now we can define the likelihood function as follows:
```math
    \begin{align*}
        & L(\theta)=\prod_{i=1}^{53}f(x_i|\theta)\\
        & L(\theta)=\prod_{i=1}^{53}\frac{2}{\theta}\left(1-e^{-\frac{x_i}{\theta}}\right)e^{-\frac{x_i}{\theta}}\\
        & L(\theta)=\left(\frac{2}{\theta}\right)^{53}\prod_{i=1}^{53}\left(1-e^{-\frac{x_i}{\theta}}\right)e^{-\frac{x_i}{\theta}}\\
        & ln(L(\theta))=53ln\left(\frac{2}{\theta}\right)+\sum_{i=1}^{53}ln\left(1-e^{-\frac{x_i}{\theta}}\right)-\sum_{i=1}^{53}\frac{x_i}{\theta}\\
        &\tag{1} ln(L(\theta))=53ln(2)-53ln(\theta)+\sum_{i=1}^{53}ln\left(1-e^{-\frac{x_i}{\theta}}\right)-\sum_{i=1}^{53}\frac{x_i}{\theta}\\
    \end{align*}
```
```math
    \begin{align*}
        &\text{Now we can differentiate the log likelihood function to find the MLE:}\\
        & \frac{d}{d\theta}ln(L(\theta))=0\\
        & \frac{d}{d\theta}\left(53ln(2)-53ln(\theta)+\sum_{i=1}^{53}ln\left(1-e^{-\frac{x_i}{\theta}}\right)-\sum_{i=1}^{53}\frac{x_i}{\theta}\right)=0\\
        & -\frac{53}{\theta}-\sum_{i=1}^{53}\frac{e^{-\frac{x_i}{\theta}}x_i}{\theta^2(1-e^{-\frac{x_i}{\theta}})}+\sum_{i=1}^{53}\frac{x_i}{\theta^2}=0\\
        &\text{here we can clearly see that the above equation is not solvable analytically, so we will use numerical methods to find the MLE.}\\
        &\text{We will use the gradient descent method to find the MLE.}\\
        &\text{The gradient descent method is an iterative method to find the minimum of a function.}\\
        &\text{The algorithm is as follows:}\\
        &\text{1. Initialize the value of $ \theta $}\\
        &\text{2. Calculate the gradient of the function at the current value of $ \theta $}\\
        &\text{3. Update the value of $ \theta $ using the formula:}\\
        &\theta_{new}=\theta_{old}-\alpha\frac{d}{d\theta}ln(L(\theta))\\
        &\text{where $ \alpha $ is the learning rate.}\\
        &\text{4. Repeat steps 2 and 3 until the value of $ \theta $ converges.}\\
        &\text{We will use the following values for the parameters:}\\
        &\text{Initial value of $ \theta $: 1}\\
        &\text{Learning rate: 0.001}\\
        &\text{We will use the following stopping criteria:}\\
        &\text{we have done it upto 1000 iterations}\\
        &\text{since our problem is maximization, we can convert it into a minimization problem by multiplying it by -1}\\
        &\text{and we also have one constant term in the equation (1) i.e 53ln2. We can discard this term because it won't affect the optimum solution. So our final equation for minimization is: }\\
    \end{align*}
```
```math
    \begin{align*}
        &\tag{2} -ln(L(\theta))=-\sum_{i=1}^{53}ln\left(1-e^{-\frac{x_i}{\theta}}\right)+\sum_{i=1}^{53}\frac{x_i}{\theta}+53ln(\theta)\\
        &\text{gradient of the function is:}\\
        &\frac{d}{d\theta}ln(L(\theta))=\sum_{i=1}^{53}\frac{e^{-\frac{x_i}{\theta}}x_i}{\theta^2(1-e^{-\frac{x_i}{\theta}})}-\sum_{i=1}^{53}\frac{x_i}{\theta^2}+\frac{53}{\theta}\\
        &\text{on further simplification we get:}\\ 
        &\frac{d}{d\theta}ln(L(\theta))=\frac{53}{\theta}+\sum_{i=1}^{53}\frac{e^{-\frac{x_i}{\theta}}x_i}{\theta^2(1-e^{-\frac{x_i}{\theta}})}-\sum_{i=1}^{53}\frac{x_i}{\theta^2}\\
        &\frac{d}{d\theta}ln(L(\theta))=\frac{1}{\theta^2}\left({53\theta}-\sum_{i=1}^{53}\frac{e^{-\frac{x_i}{\theta}}x_i}{(1-e^{-\frac{x_i}{\theta}})}-\sum_{i=1}^{53}{x_i}\right)\\
        &\text{we will use the above equation to find the MLE using the gradient descent method. By using the below equation:}\\
        &\theta_{new}=\theta_{old}-\alpha\frac{d}{d\theta}ln(L(\theta))\\
        &\text{by using the above equation we can find the MLE of $ \theta $}\\
    \end{align*}
```
using the above equation with specified parameters, we have found that the MLE is converging to 0.5 as we can see in the below graph:
![alt text](image-1.png)