import numpy as np
from scipy.odr import exponential


######################### NumPy ufunc Create ###################################
def myadd(x,y):
    return x + y

myadd = np.frompyfunc(myadd,2,1)

print(myadd([1,2,3,4,5],[4,5,6,6,7]))


print(type(np.add))


if type(np.add)== np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')

print()
print()
print()
print()
print()
print()



#################################      NumPy ufunc Simple Arithmetic ###############################

arr1 = np.array([12,3,4,45,5])

arr2 = np.array([1,2,44,45,6])

add_result = np.add(arr1,arr2)
print("addition result:", add_result )


subtract_result = np.subtract(arr1,arr2)
print("subtract result:", subtract_result )

multiply_result = np.multiply(arr1,arr2)
print("multiplication result:",multiply_result)

divide_result = np.divide(arr1,arr2)
print("division result:",divide_result)

scalar_multiply = np.multiply(arr1,2)
print("scalar multiplication result: ",scalar_multiply)

print()
print()
print()
print()
print()
print()


######################################   NumPy ufunc Rounding Decimals #################################

decimal_array = np.array([3.122132, 3.546576, 2.3243534, 5.34123124])
rounded_array = np.round(decimal_array,decimals=2)
print('Rounded array:',rounded_array)

arounded_array = np.around(decimal_array,decimals=1)
print('Around array:',arounded_array)

print()
print()
print()
print()
print()
print()

######################### NumPy ufunc Logs #########################


numbers_array =np.array([1,2,3,4,5])

logarithimic_result = np.log(numbers_array)
print("logarithimic result:",logarithimic_result)


exponential_result = np.exp(numbers_array)
print("exponential result:",exponential_result)

log_base_10_result = np.log10(numbers_array)
print("log base 10 result:",log_base_10_result)


print()
print()
print()
print()
print()
print()

###################################   NumPy ufunc Summations ###################################


data_array = np.array([10,20,30,40,50])

sum_result = np.sum(data_array)
print("Summation result",sum_result)

axis_sum_result = np.sum(data_array,axis=0)
print("axis 0 Summation result",sum_result)


#cummalatative sum function
arr = np.array([1,2,3,4,5])
newarr = np.cumsum(arr)
print(newarr)



################################### NumPy ufunc Products ################################

data_array = np.array([1,2,3,4,5])

product_result = np.prod(data_array)
print("result",product_result)


axis_product_result = np.prod(data_array,axis=0)
print("along axis result",axis_product_result)

array = np.array([1,2,3,4,5])
new_array = np.cumprod(array) #cummalatative product
print(new_array)










