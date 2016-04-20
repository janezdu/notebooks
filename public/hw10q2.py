'''
X is a uniformly distributed RV over [1,0]
g(x) = e^(-sqrt(1 - x^2))/sqrt(x)
'''
import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return np.e**(-np.sqrt(1 - x**2))/np.sqrt(x)


def f(x):
    return np.sqrt(x)**(-1)


num = 1500
uni = np.random.uniform(0, 1, num)

# f(x) = 1
sum = 0
factor = 1
naiveaverage = []

for i in range(1, num):
    sum += g(uni[i])
    naiveaverage.append(factor * sum/i)


# f(x) = 1/(sqrt(x))
sum = 0
factor = 2  # calculated by hand
plotaverages = []
distr = uni**2

for i in range(1, num):
    sum += g(distr[i])/f(distr[i])
    plotaverages.append(factor * sum/i)

# actual value
plt.axhline(y=0.85174, color='k', linestyle='dashed')
# mc integration
plt.plot(plotaverages)
plt.plot(naiveaverage, c='r')

# other graph details
plt.xlabel('Sample Size')
plt.ylabel('Approximation')
plt.title("Comparing f(x) = 1 [red] and f(x) = 1/sqrt(x) [blue]")
plt.axis([0, num, .5, 1.2])
plt.grid(True)

plt.show()
