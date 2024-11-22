import numpy as np

#one dimesional array
x = np.array([1,2,3,4])

#List [1,2,3,4]
#Tuple (1,2,3,4)


print(x)


#two dimesional array
y = np.array([[1,2,3,4],[1,2,3,4]])
print(y)

#three dimesional array
z = np.array([[[1,2],[4,5]],[[6,7],[8,9]]])
print(z)


print(x.ndim)

print(y.ndim)
#check dimesion
print(z.ndim)



#reppresent by four dimensional array using "ndimn" dimesional array
z = np.array([1,2,3,4],ndmin=4)

print(z)

print(z.ndim)

#Array Indexing
arr = np.array((1,2,3,4))
print(arr)
print(arr[2])

print(arr[2]+arr[3])


#Multi dimensional Array Indexing

arr = np.array([1,2,3,4])
print(arr)
print(arr[2])

print(arr[2]+arr[3])


#2D array indexing
arr = np.array([[1,2,3],[2,2,4],[3,6,8]])

print(arr)
#arr[row,column]
print(arr[1,0])


#3D array indexing
arr = np.array([[[1,2,3],[2,2,4]],[[1,2,3],[2,2,4]]])

print(arr)

print(" Dimension :" )
print(arr.ndim)

#arr[array,row,column]
print(arr[1,1,2])


#negative indexing      -4  -3  -2 -1
#index                  0 1 2 3

arr = np.array([1,2,3,4])

print(arr[1])
print(arr[-3])


#Array Slicing

x = np.array([1,2,3,4])

#x[start:end]
print(x[1:3])
# end number index does not print
print(x[-3:-1])


print(x[1:])#first index to end


print(x[:2])#zero to first index

x = np.array([1,2,3,4,5,6,7,8])
#x[start:end:step]
print("even",x[1::2])
print("odd",x[::2])


arr = np.array([[1,2,3],[2,2,4],[3,6,8]])
print(arr)
print(arr[1,2])
print(arr[1,1:])#1st index row and 1 column to end cloumn
print(arr[:,2])#all row and 2 column print



#Data Types in numpy (integer(i),float(f),boolean(b),complex(c),string(unicode string - U), time delta(m), date time(M), object(O) )
x = np.array([1,2,3,4,5,6,7,8])
print(x)
print(x.dtype)#check datatype


x = np.array(["s","saas","green"])
print(x)
print(x.dtype)#check datatype


#integer array convert to float
x = np.array([1,2,3,4,5,6,7,8],dtype='f')
print(x)
print(x.dtype)#check datatype

#integer array convert to string
x = np.array([1,2,3,4,5,6,7,8],dtype='U')
print(x)
print(x.dtype)#check datatype



#integer array convert to float using inbuild function "astype"
x = np.array([1,2,3,4,5,6,7,8])
print(x)
print(x.dtype)#check datatype

y = x.astype('f')
print(y)
print(y.dtype)


#float array convert to integer using inbuild function "astype"
x = np.array([1., 2., 3. ,4. ,5., 6., 7. ,8.])
print(x)
print(x.dtype)#check datatype

y = x.astype('i')
print(y)
print(y.dtype)

#float or integer array convert to bool using inbuild function "astype"
x = np.array([1., 2., 0 ,4. ,5., 6., 7. ,8.])
print(x)
print(x.dtype)#check datatype

y = x.astype('bool')
print(y)
print(y.dtype)



####Copy Vs View
#copy
print('copy')


x = np.array([1,2,3,4])
y=x.copy()

print(x)
print(y)

print('Original array or not :',y.base)#if original it will print array if not original print none


x[0]=9

print(x)
print(y)

print('Original array or not :',y.base)#if original it will print array if not original print none


print()
print()

print('view')

#view
x = np.array([1,2,3,4])
y=x.view()
print(x)
print(y)

print('Original array or not :',y.base)#if original it will print array if not original print none


x[0]=9

print(x)
print(y)

print('Original array or not :',y.base)#if original it will print array if not original print none

#view function connect original array when changes happend it will affect view array also

#but copy() function not happend like that



print('Iterating' )
#Iterating
arr = np.array([[1,2,3],[4,5,6]])

for i in arr:
    for j in i:
        print(j)


print()
print()
print()
print()
print('nditer()')
#numpy function use in arrays access into single elements in multidimentional array nditer()
arr = np.array([[1,2,3],[4,5,6]])

for i in np.nditer(arr):
    print(i)



print()
print("how to access different styles in array")
#(start:end:step)
for i in np.nditer(arr[:, ::2]):
    print(i)


#print index number "ndenamerate() "
print()
print("print index number ndenamerate()")
#(start:end:step)
for i,j in np.ndenumerate(arr):
    print(i,j)
#i - index number
#j - elemnet






#Shape and Reshape "
print()
print("Shape and Reshape")
#shape -  returns a tuple with each index having the number of corresponding elements
#2D array
arr = np.array([[1,2,3,4],[5,6,7,8]])

print(arr)
print(arr.shape)

print()
print()
print()
print()
print()

#3D array
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr)
print(arr.shape)

print()
print()
print()
print()

#use ndmin to  create  array what dimension we need
x = np.array([1,2,3,4],ndmin=5)
print(x)

print(x.shape)



print()
print()
#Reshape
print()
print("  Reshape")
#shape -  returns a tuple with each index having the number of corresponding elements
#2D array
x = np.array([1,2,3,4,5,6,7,8])

print(x)


print()

new= x.reshape(2,4)
print(new)

print()
#2D array

new= x.reshape(8,1)
print(new)




print()
#3D array
new= x.reshape(2,2,2)
print(new)


print()
#if we can not this what dimension is use -1 ,then it will do automatically assign dimension
new= x.reshape(2,2,-1)
print(new)


print()

new= x.reshape(2,-1)
print(new)

print()
print()

print()
#any dimesion array convert into 1D array
new= x.reshape(-1)
print(new)


print()
print()
print()
print()
print()
print()
print()


#######################      Numpy Array Reshaping          ###########################

origina_array = np.array([1,2,3,4,5,6])

row_major = origina_array.reshape(2,3,order='C')

column_major = origina_array.reshape(2,3,order='F')

reshaped_array = origina_array.reshape(2,3)


print('origina_array : ')
print(origina_array)
print()
print('row_major : ')
print(row_major)
print()
print('column_major : ')
print(column_major)
print()
print('reshaped_array : ')
print(reshaped_array)
print()








print()
print()
print()
print()
print()
print()
print()

################  array view and shape #######################

original_array = np.array([[12,34,54],[21,43,24]])

array_view = original_array.view()

array_view.shape = (3,2)

print('Original array :')

print(original_array)
print('Array View :')
print(array_view)

print()
print()
print()
print()
print()






print()
print()
print()
print()
print()
print("Search elements")
print()
#1D array
arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr==4)
print(arr)
print(x)#output index number

print()
#2D array
arr = np.array([[1,2,3,4],[5,6,7,8]])
x = np.where(arr==4)

print(arr)

print(x)#output index number




print()
print("get even numbers using np.where")
#1D array
arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2==0)
print(arr)
print("print index numbers in even numbers")
print(x)#output index numbers



print()
print()
print()
print()
print("Searchsorted()")
#1D array
arr = np.array([1,2,3,5,8])
x = np.searchsorted(arr, 4 )
print(arr)
print("print index numbers need to add number in array ")
print(x)#output index numbers


print()

#1D array
arr = np.array([1,2,3,5,8])
x = np.searchsorted(arr, [2,4,8])
print(arr)
print("print index numbers need to add numbers in array ")
print(x)#output index numbers


print()

#1D array
arr = np.array([1,2,3,5,8])
x = np.searchsorted(arr, 4, side='right' )
#using place to take right side
print(arr)
print("print index numbers need to add numbers in array in right consideration ")
print(x)#output index numbers







print()
print()
print()
print()
print()
print("Join and Split")
print()


arr1= np.array([1,2,5])
arr2 = np.array([4,7,8])

#join two arrays
newarr= np.concatenate((arr1,arr2))
print(newarr)


print()

#2D arrays
arr1= np.array([[1,2,5],[4,5,6]])
arr2 = np.array([[4,7,8],[9,10,11]])

#join two arrays
newarr= np.concatenate((arr1,arr2))
print(newarr)

print()

#2D arrays
arr1= np.array([[1,2,5],[4,5,6]])
arr2 = np.array([[4,7,8],[9,10,11]])

#join two arrays
#default axis =0
newarr= np.concatenate((arr1,arr2),axis=1)
print(newarr)

print()
print()
print('np.array_split() using split arrays')
arr = np.array([1,2,3,4,5,6,7,8])

newarr = np.array_split(arr,3)
print("split 3 sections",  newarr)


print()
newarr = np.array_split(arr,2)
print("split 2 sections",  newarr)

print()
newarr = np.array_split(arr,4)
print("split 4 sections",  newarr)