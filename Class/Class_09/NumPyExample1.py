# Luke Reed
# NumpyExample1.py
# 03/17/2016
# a brief introduction to numpy

import numpy as np

print(np.pi)
print(np.e)

a = np.array([1,4,5,8], float)
print(a)
print(type(a))

a = np.array([[1,2,3],[4,5,6]], float)
print(a)
print(len(a))
print(a.shape)
print("Matrix Transpose")
print(a.transpose())

a = np.array([1,2,3], float)
b = np.array([5,2,6], float)
print("Matrix Addition and Multiplication")
print(a+b)
print(a*b)

a = np.array([[4,2,0],[9,3,7],[1,2,1]], float)
print("Matrix Determinant")
print(np.linalg.det(a))
vals, vecs = np.linalg.eig(a)
print("Eigen Values & Eigen Vectors")
print(vals,vecs)
b = np.linalg.inv(a)
print("Matrix Inverse")
print(b)

a = np.array([1,4,3,8,9,2,3], float)
print("Median Value")
print(np.median(a))

print("Roots of Polynomial x**2 - 9")
print(np.roots([1,0,-9]))
print("Roots of Polynomial x**3 + 4x**2 -2x +3")
print(np.roots([1,4,-2,3]))

x = [1,2,3,4,5,6,7,8]
y = 0,2,1,3,7,10,11,19
print("Polynoimial Fit - 1")
print(np.polyfit(x,y,2))		# 2 makes it a linear regression

x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4,5,6,7,8]
print("Polynomial Fit - 2")
print(np.polyfit(x,y,2))

