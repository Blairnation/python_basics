import numpy as np
from numpy import random
from matplotlib import pyplot as plt
import seaborn as sns
from math import log

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr = np.array([1, 2, 3, 4], ndmin=5)  # giving it number of dimensions

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(type(a))

# Accessing 1D array elements
arr1 = np.array([1, 2, 3, 4])
print(arr1[1])
print(arr1[2] + arr1[3])

# Accessing 2D array elements
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('third element in second row', arr2[1, 3])

# Accessing 3D array elements
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3[0, 1, 2])  # 6

# negative indexing
arr_neg = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('Last element from 2nd dim: ', arr_neg[1, -1])

# slicing
arr_slice = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr_slice[1:5:2])  # [start:end(exclusive):step]

# 2D slicing
arr_2d_slice = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr_2d_slice[1, 1:4])  # [elements, indexing]

# 2D slicing elements to produce index
ar_2d_slice = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(ar_2d_slice[0:2, 2])  # From both elements, return index 2

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
ar_2d_slicing = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(ar_2d_slicing[0:2, 1:4])

# changing datatype of array
arr3 = np.array([1.1, 2.2, 3.9, 4.0], dtype='S')  # change to string
# or using .astype(change datatype)
tape = arr3.astype('i')  # or
# tape = arr3.astype(int)
print(tape.dtype)

# copy and view attributes
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()  # copies array and can be changed
y = arr.view()  # views the original array
# base attribute to deter whether it owns itself or not
print(x.base)  # copy owns itself, returns none
print(y.base)  # view doesn't own itself, returns array

# shape (no of elements in each dimension)
arr = np.array([5, 6, 7, 8], ndmin=5)

print(arr.shape)  # prints (1,1,1,1,4)

# iterating and bringing out all elements in an array
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

# change datatype of all arrays in an iteration
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# finding index and value using ndenumerate

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for i, value in np.ndenumerate(arr):
    print(i, value)
print()
print(arr[1, 0, 2])

arr2 = np.array([1, 2, 3])
for i, value in np.ndenumerate(arr2):
    print(i, value)

# suggestions
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for i, value in np.ndenumerate(arr):
    print(i, value)
print()
print(arr[1, 0, 2])

arr2 = np.array([1, 2, 3], ndmin=5)
for i, value in np.ndenumerate(arr2):
    print(i, value)
print(arr2.ndim)

print()
print(arr2.shape)
print(arr.shape)

# concatenation
arr1 = np.array([[1, 2, 3, 4], [10, 20, 30, 40]])
arr2 = np.array([[1, 2, 3, 4], [60, 57, 38, 70]])
arr3 = np.array([1, 2, 3, 4])

arr = np.concatenate((arr1, arr2), axis=1)  # axis=0 for vertical(along rows) and axis=1 for horizontal concatenation
print(arr)

# stacked and concatenate
import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([[1, 2, 3, 4], [60, 57, 38, 70]])
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([[1, 2, 3, 4], [60, 57, 38, 70]])

arr = np.stack((arr1, arr3))
arc = np.concatenate((arr1, arr3))
print(arr)
print()
print(arc)
print()

arr = np.stack((arr1, arr3), axis=1)
arc = np.concatenate((arr2, arr4), axis=1)
print(arr)
print()
print(arc)

# suggestions 2
import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([[1, 2, 3, 4],
                 [60, 57, 38, 70]])
arr4 = np.array([[1, 2, 3, 4],
                 [60, 57, 38, 70]])

arr = np.concatenate((arr1, arr2))
print(arr)
print()
arr = np.concatenate((arr3, arr4))
print(arr)
print()
arr = np.concatenate((arr3, arr4), axis=1)
print(arr)
print()
arr = np.stack((arr1, arr2))
print(arr)
print()
arr = np.stack((arr3, arr4))
print(arr)
print()

# hstack(rows) and vstack(column)
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([[1, 2, 3, 4],
                 [60, 57, 38, 70]])
arr4 = np.array([[1, 2, 3, 4],
                 [60, 57, 38, 70]])

arr = np.hstack((arr1, arr2))
print(arr)
print()
arr = np.vstack((arr1, arr2))
print(arr)
print()

arr = np.hstack((arr3, arr4))
print(arr)
print()

# Array split
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 2)
print(new_arr)
print(new_arr[0])  # Accessing elements of split array
print(new_arr[1])

# vsplit, hsplit, dsplit
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.vsplit(arr, 3)  # np.hsplit

print(newarr)

# search array (bring the indexes)
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
# even numbers index check
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr % 2 == 0)  # odd numbers (arr % 2 == 1)
print(x)

# search where(index) number should be in sorted order
arr = np.array([6, 4, 8, 9])
x = np.searchsorted(arr, 7)  # add(side ='right') to start sorted from right
print(x)

# sort
arr = np.array([[3, 2, 4], [5, 0, 1]])
x = np.sort(arr)
print(x)

# filter (boolean)
# 1
arr = np.array([41, 42, 43, 44, 23, 56, 67])

x = [True, False, True, False, True, True, False]

print(arr[x])
# 2
filter_list = []
for item in arr:
    if item >= 43:  # if item % 2 == 0: for even numbers and many more
        filter_list.append(True)
    else:
        filter_list.append(False)
x = arr[filter_list]
print(x)

# filter directly from array
arr = np.array([41, 42, 43, 44, 23, 56, 67])

filter_arr = arr > 41

new_arr = arr[filter_arr]
print(new_arr)

# chapter 2

# probability using numpy random module
arr = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(arr)

# shuffling array using random
arr = np.array([2, 3, 4, 5, 6, 7, 8])
random.shuffle(arr)
print(arr)

# using permutation
arr = np.array([1, 2, 3, 4, 5])
x = random.permutation(arr)
print(x)

# distribution plot(using seaborn and matplotlib)

# random normal(mean,standard deviation,size)
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
sns.distplot(x, hist=False)  # Removing histogram
plt.show()

# random binomial(no of trial(n),probability(p),size)
x = random.binomial(n=10, p=0.5, size=1000)
sns.distplot(x, hist=True, kde=False)
plt.show()

# showing normal and binomial together
x = random.binomial(n=100, p=0.5, size=1000)
y = random.normal(loc=50, scale=5, size=1000)
sns.distplot(x, hist=False)
sns.distplot(y, hist=False)
plt.show()

# random poisson (generate values around the mean(lam) value)
x = random.poisson(lam=2, size=10)
print(x)

# random uniform(generate 0 to 1)
x = random.uniform(size=(2, 3))
print(x)
sns.distplot(x, hist=False)
plt.show()

# random logistic(small deviation from mean)
x = random.logistic(loc=1, scale=2, size=1000)
print(x)
sns.distplot(x, hist=False)
plt.show()

# random multinomial (probability more than two occurrences)
x = random.multinomial(n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
print(x)

# random exponential (time till next event)
x = random.exponential(scale=2, size=1000)
print(x)
sns.distplot(x, hist=False)
plt.show()

# chi square (basics of hypothesis)
x = random.chisquare(df=1, size=1000)
print(x)
sns.distplot(x, hist=False)
plt.show()

# random rayleigh (signal processing)
x = random.rayleigh(scale=2, size=1000)
print(x)
sns.distplot(x, hist=False)
plt.show()

# random pareto
x = random.pareto(a=1, size=1000)
print(x)
sns.distplot(x, kde=False)
plt.show()

# zipf (sample 1000 but plot ones value > 10)
x = random.zipf(a=2, size=1000)
print(x)
sns.distplot(x[x < 10], kde=False)
plt.show()

# ufuncs
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
# z = np.subtract(x, y) # subtraction
# z = np.multiply(x,y) # multiplication
# z = np.divide(x,y) # division
# z = np.power(x, y) # power
# z = np.mod(x, y) # mod = remainder
# z = np.remainder(x, y) # remainder
# z = np.divmod(x, y) # return quotient and mod
# z = np.abs/absolute(x, y) # return positive array elements if negative
print(z)


# or frompyfunc
def myadd(x, y):
    return x + y


myadd = np.frompyfunc(myadd, 2, 1)  # takes function and takes 2 array input and bring out 1 array as output
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# rounding
arr = np.fix([-3.1666, 3.6667]) # removes decimal and return floating point
# OR arr = np.trunc([-3.1666, 3.6667])
# arr = np.floor([-3.1666, 3.6667]) # nearest lower integer
# arr = np.ceil([-3.1666, 3.6667]) # nearest upper integer
print(arr)
# around(arg, decimal places)
arr = np.around(3.1666, 2)
print(arr)

# log
arr = np.arange(1, 10)  # range of array 1 to 10(exclusive)
print(np.log2(arr))  # base2
print(np.log10(arr))  # base10

# log (other bases)
nplog = np.frompyfunc(log, 2, 1)  # takes log function and 2 inputs and 1 output
print(nplog(100, 15))  # log 100  to base 15

# lcm of array members
arr = np.array([3, 6, 9])
# x = np.arange(1,10)
x = np.lcm.reduce(arr)  # same for gcd = np.gcd.reduce
print(x)

# create set array
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
# union 1d
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
# intersect 1d
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
# newarr = np.setdiff1d(arr1, arr2,assume_unique=True) in set 1 and not in set 2 and vice versa
# newarr = np.setxor1d(arr1, arr2,assume_unique=True) only in one set (not in both)
print(newarr)

