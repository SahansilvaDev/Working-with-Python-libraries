
import numpy as np

from numpy import random


####################    Numpy Random Data Distribution        ########################

x = random.choice([5,6,9,8],p=[0.2,0.7,0.1,0.0],size=(100))
print(x)
print()
print()
print()
print()
x = random.choice([5,6,9,8],p=[0.2,0.7,0.1,0.0],size=(3,5))
print(x)
print()
print()
print()


# Generate 10 random values uniformly distributed in [0, 1)
data = np.random.rand(10)
print(data)

print()
print()


########################      Numpy Random Permutations       ###################################

# Shuffle a given array
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)

print('random shuffle',arr)

shuffled = np.random.permutation(arr)
print('random permutation; ',shuffled)


print()

print()

# Shuffle a given array
arr = np.array([[1, 2,6],[2,3,5], [3, 4, 5]])
shuffled = np.random.permutation(arr)
print('random permutation Rows; ',shuffled)

shuffled = np.random.permutation(arr.T).T
print('random permutation Columns; ',shuffled)



print()

# Generate a random permutation of integers from 0 to 9
perm = np.random.permutation(10)
print(perm)


print()
print()




######################       seaborn             ############################


import seaborn as sns
import matplotlib.pyplot as plt


print()
print()

sns.displot([0,1,2,3,4,5])
plt.show()



sns.displot([0,1,2,3,4,5], kind="kde")
plt.show()



print()
print()

##########################      Numpy Normal Distribution    #################################


x = random.normal(size=(2,3))
print(x)


print()
print()



#loc = mean , scale = standard deviation
x = random.normal(loc=1, scale=2, size=(2,3))
print(x)


print()
print()

data = sns.displot(np.random.normal(size=1000))
plt.show()



data = sns.displot(np.random.normal(size=1000), kde=True)
plt.show()



print()
print()

# Random normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)
sns.histplot(data, kde=True)
plt.show()



print()
print()

# Generate data from a normal distribution
data = np.random.normal(loc=0, scale=1, size=10)
print(data)

####################      Binomial distribution      ###################
n,p, size = 10,0.5,1000
data=np.random.binomial(n,p,size)
count , bins, ignored = plt.hist(data,11,density=True)
plt.title("Binomial distribution")
plt.show()


sns.displot(random.normal(loc=50,scale=5,size=1000),kind="kde",label='normal')
sns.displot(random.binomial(n=100,p=0.5,size=1000),kind="kde",label='binomial')
plt.title("Normal VS Binomial distribution")
plt.show()


print()
print()
print()

# Binomial distribution: 10 trials, probability of success = 0.5
data = np.random.binomial(n=10, p=0.5, size=10)
print("binomial distribution")

print(data)





print()
print()
print()
print()




####################      Poisson distribution       ###################

# Poisson distribution: mean number of events = 3
data = np.random.poisson(lam=3, size=10)
print("Poisson distribution")
print(data)


sns.displot(random.poisson(lam=2,size=1000),kde=False)
plt.title("Poisson distribution")
plt.show()
print()



sns.displot(random.normal(loc=50,scale=7, size=1000),kind='kde',label='normal' )
sns.displot(random.poisson(lam=2,size=1000),kind='kde')
plt.title("Poisson VS Normal distribution")
plt.show()
print()

print()
print()
print()
print()


####################      Uniform distribution       ###################

# Uniform distribution in range [0, 5)
data = np.random.uniform(low=0, high=5, size=10)
print('Uniform distribution')
print(data)


print()
print()
print()
print()

data = np.random.uniform(size=(5,3))
print('Uniform distribution')
print(data)

print()
print()
print()
print()


sns.displot(np.random.uniform(size=(5,3)))
plt.title('Uniform distribution')
plt.show()


sns.displot(np.random.uniform(size=1000))
plt.title('Uniform distribution')
plt.show()


sns.displot(np.random.uniform(size=1000),kind='kde')
plt.title('Uniform distribution')
plt.show()

