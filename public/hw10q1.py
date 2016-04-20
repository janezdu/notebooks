'''
X is a uniformly distributed RV over [1,0]
I_f = 1
g(x) = e^(-sqrt(1 - x^2))/sqrt(x)
'''
import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return np.e**(-np.sqrt(1 - x**2))/np.sqrt(x)

# sample
num = 150
uni = np.random.uniform(0, 1, num)
distr = uni

sum = 0
naiveaverage = []

for i in range(1, num):
    sum += g(distr[i])
    # print(sum/i)
    naiveaverage.append(sum/i)

print(sum/num)

# actual value
plt.axhline(y=0.85174, color='k', linestyle='dashed')
# mc integration
plt.plot(naiveaverage)

# other graph details
plt.xlabel('Sample Size')
plt.ylabel('Approximation')
plt.title(r'$f(x) = 1$')
plt.axis([0, num, 0.5, 1.5])
plt.grid(True)

plt.show()
