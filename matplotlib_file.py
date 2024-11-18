import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,2,5])
plt.show()



plt.plot([1,2,3],[4,2,5])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Simple Graph')
plt.show()


import numpy as np
x = [1,2,3,4,4,5,6,6,7]
plt.plot(x,np.power(x,2))
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Example')
plt.show()

####color changing characters####
# Blue  'b'
# Green 'g'
# Red  'r'
# Cyan 'c'
# Magenta 'm'
# Yellow  'y'
# Black  'k'
# White 'w'

 ####point markers####
# Point marker '.'
# Circle marker 'o'
# X marker  'x'
# Diamond marker  'D'
# Hexagon marker  'H'
# Square marker  's'
# Plus marker  '+'

####Line Style ####
# Solid line '-'
# Dashed line '_'
# Dash-dot line '-.'
# Dotted line ':'
# Hexagon marker 'H'

#Adding color marker and line style
x = [1,2,3,4,4,5,6,6,7]
#plt.plot(x,y,'color,marker,line style')
plt.plot(x,np.power(x,2),'k^-.')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Adding color marker and line style')
plt.show()



#line width changing
x = [1,2,3,4,4,5,6,6,7]
#plt.plot(x,y,'color,marker,line style')
plt.plot(x,np.power(x,2),'k^-.',linewidth=10)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('line width changing')
plt.show()


#one figure draw two lines
x = [1,2,3,4,4,5,6,6,7]
#plt.plot(x,y,'color,marker,line style')
plt.plot(x,np.power(x,2),'k^-.',x,np.power(x,3),'c+:')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('one figure draw two lines')
plt.show()


#knowing Limits of axis
plt.plot([1,2,3,4],[4,2,6,8])
left,right = plt.xlim()
print(left)
print(right)
plt.title('knowing Limits of axis')
plt.show()

#changing Limits of axis
plt.plot([1,2,3,4],[4,2,6,8])
left,right = plt.xlim(2,7)#plt.xlim('x axis left conrner','x axis right corner')
print(left)
print(right)
plt.title('changing Limits of axis 2 to 7')
plt.show()

#changing only Limits of x axis left corner
plt.plot([1,2,3,4],[4,2,6,8])
left,right = plt.xlim(2)#plt.xlim('x axis left conrner')
print(left)
print(right)
plt.title('changing only Limits of x axis left corner as 2')
plt.show()

#changing only Limits of x axis right corner
plt.plot([1,2,3,4],[4,2,6,8])
left,right = plt.xlim(right= 7)#plt.xlim(right = 'x axis right corner')
print(left)
print(right)
plt.title('changing only Limits of x axis right corner as 7')
plt.show()


#changing Limits of x axis
plt.plot([1,2,3,4],[4,2,6,8])
left,right = plt.xlim(left=2, right= 7)#plt.xlim(left = x axis left conrner' , right = 'x axis right corner')
print(left)
print(right)
plt.title('changing Limits of x axis 2 to 7')
plt.show()


#changing  Limits of y axis bottom and top
plt.plot([1,2,3,4],[4,2,6,8])
bottom,top = plt.ylim()#plt.ylim(bottom = y axis bottom ' , right = 'y axis top ')
print(bottom)
print(top)
plt.title('changing  Limits of y axis bottom and top defalut')
plt.show()


#changing  Limits of y axis bottom and top
plt.plot([1,2,3,4],[4,2,6,8])
bottom,top = plt.ylim(2,7)#plt.ylim(bottom = y axis bottom ' , right = 'y axis top ')
print(bottom)
print(top)
plt.title('changing  Limits of y axis bottom and top 2 to 7')
plt.show()


#changing  Limits of y axis bottom and top
plt.plot([1,2,3,4],[4,2,6,8])
bottom,top = plt.ylim(bottom= 1,top= 7)#plt.ylim(bottom = y axis bottom ' , right = 'y axis top ')
print(bottom)
print(top)
plt.title('changing  Limits of y axis bottom and top 1 to 7')
plt.show()

############# Subplots ################
x = np.arange(1,10,0.1)
y1 = x
y2 = np.sqrt(x)
y3 = np.power(x,2)
y4 = np.power(x,3)
plt.figure()

#plt.subplot(row,column,plot number)
plt.subplot(2,2,1)
plt.plot(x,y1,'ro')
plt.title('y1 = x')

plt.subplot(2,2,2)
plt.plot(x,y2,'g--')
plt.title('$y2 =\sqrt{x}$')


plt.subplot(2,2,3)
plt.plot(x,y3,'b^')
plt.title('y1 = x')

plt.subplot(2,2,4)
plt.plot(x,y4,'ks')
plt.title('$y4 = x^3 $')

plt.show()


##############      Line chart & Bar chart        ##################
age = [10,20,30,40,50,60,70]
weight = [40,25,38,45,55,85,72]
plt.plot(age, weight)
plt.title('Line chart')
plt.show()


subjects = ['maths','physics','chemisty']
marks = [80,75,78]
plt.bar(subjects, marks)
plt.title('Bar chart')
plt.show()


#add or reduce width in bars
subjects = ['maths','physics','chemisty']
marks = [80,75,78]
plt.bar(subjects, marks,width=0.4)
plt.title('reduce width in bars - Bar chart')
plt.show()


#horizontal representation
subjects = ['maths','physics','chemisty']
marks = [80,75,78]
#barh
plt.barh(subjects, marks)
plt.title('horizontal representation - Bar chart')
plt.show()

#############    Histogram for frequencies to display ##############

marks = [12,3,34,5,56,76,7,89,54,78,68,67,67,67,67]
plt.hist(marks)
plt.title("Histogram")
plt.show()


#need to divide parts 'bins = 4'
marks = [12,3,34,5,56,76,7,89,54,78,68,67,67,67,67]
plt.hist(marks,bins=4)
plt.title("Histogram")
plt.show()


#need to divide points 'bins=[0,25,50,100]'
marks = [12,3,34,5,56,76,7,89,54,78,68,67,67,67,67]
plt.hist(marks,bins=[0,25,50,100])
plt.title("Histogram")
plt.show()


#relative width (adjust gap)
marks = [12,3,34,5,56,76,7,89,54,78,68,67,67,67,67]
plt.hist(marks,bins=[0,25,50,100],rwidth=0.9)
plt.title("Histogram")
plt.show()



#add color
marks = [12,3,34,5,56,76,7,89,54,78,68,67,67,67,67]
plt.hist(marks,bins=[0,25,50,100],rwidth=0.9,color='r')
plt.title("Histogram")
plt.show()


#################       Pie Chart      ###################

category = ['food','transport','rent','other']
cost = [900,850,1500,400]
plt.pie(cost,labels=category) #plt.pie(values,labels)
plt.show()


#add sizes --- radius
category = ['food','transport','rent','other']
cost = [900,850,1500,400]
plt.pie(cost,labels=category,radius=1.5) #plt.pie(values,labels,size)
plt.show()

#add percentage
category = ['food','transport','rent','other']
cost = [900,850,1500,400]
plt.pie(cost,labels=category,radius=1.5,autopct='%f%%') #plt.pie(values,labels,size,auto percentage)
plt.show()

#add percentage one decimal point
category = ['food','transport','rent','other']
cost = [900,850,1500,400]
plt.pie(cost,labels=category,radius=1.5,autopct='%0.1f%%') #plt.pie(values,labels,size,auto percentage)
plt.show()

#add add highlight
category = ['food','transport','rent','other']
cost = [900,850,1500,400]
plt.pie(cost,labels=category,radius=1.5,autopct='%0.1f%%',explode=[0,0.1,0,0]) #plt.pie(values,labels,size,auto percentage,highlight label[label1,label2,label3.label4])
plt.show()

