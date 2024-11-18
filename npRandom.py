import numpy as np

# Generate 10 random values uniformly distributed in [0, 1)
data = np.random.rand(10)
print(data)



# Shuffle a given array
arr = np.array([1, 2, 3, 4, 5])
shuffled = np.random.permutation(arr)
print(shuffled)

# Generate a random permutation of integers from 0 to 9
perm = np.random.permutation(10)
print(perm)



import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Random normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)
sns.histplot(data, kde=True)
plt.show()




# Generate data from a normal distribution
data = np.random.normal(loc=0, scale=1, size=10)
print(data)


# Binomial distribution: 10 trials, probability of success = 0.5
data = np.random.binomial(n=10, p=0.5, size=10)
print(data)


# Poisson distribution: mean number of events = 3
data = np.random.poisson(lam=3, size=10)
print(data)



# Uniform distribution in range [0, 5)
data = np.random.uniform(low=0, high=5, size=10)
print(data)
