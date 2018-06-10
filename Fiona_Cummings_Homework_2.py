
# coding: utf-8

# In[1]:

import numpy as np


# In[15]:

#Create matrix A with size (3,5) containing random numbers
A = np.matrix(np.random.random(15)).reshape(3,5)
A


# In[19]:

#Find the size and length of matrix A
#find size

A.size


# In[20]:

#find length
len(A)


# In[37]:

#Resize (crop/slice) matrix A to size (3,4) & re-assign A to resized object

A = np.resize(A,(3,4))

A


# In[160]:

#Find the transpose of matrix A and assign it to B

B = A.transpose()

B


# In[54]:

#Find the minimum value in column 1 of matrix B (check the proper4es of a matrix – ‘B.min()’)
#assuming this means this means finding the minimum of the first column, index 0, not column with the index of 1

B.min(0)[0]


# In[56]:

#Find the minimum and maximum values for the en4re matrix A
#find max
A.max()


# In[57]:

#find min
A.min()


# In[60]:

#Create vector X (an array) with 4 random numbers

x = np.array([np.random.random(4)])

x


# In[138]:

#Create a func4on and pass vector X and matrix A in it
#In the new func4on mul4ply vector X with matrix A and assign the result to D

def function(var1, var2):
    D = var1*var2
    return D

function(x, A)


# In[139]:

#Create a complex number Z with absolute and real parts != 0

Z = 2+15j


# In[140]:

Z.real


# In[141]:

Z.imag


# In[142]:

abs(Z)


# In[143]:

#Mul4ply result D with the absolute value of Z and record it to C
D = function(2,4)


# In[147]:

C = D*abs(Z)
C


# In[161]:

#Convert matrix B from a matrix to a string and overwrite B

B = str(B.flatten())

B


# In[163]:

#Display a text on the screen: ‘Your Name is done with HW2‘

print "Fiona is done with HW2!"


# In[ ]:



