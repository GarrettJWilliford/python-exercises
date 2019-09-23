import numpy as np


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


def check_negative(inp):
    return len(inp[inp < 0])

def check_positive(inp):
    return len(inp) - check_negative(inp)


def even_positive(inp):
    inp = inp[inp % 2 == 0]
    return sum(inp >= 0)

def add_3(inp):
    return sum(inp + 3 >= 0)


def square(inp):
    inp = inp ** 2
    return inp.mean(), inp.std()

def zscore(inp):
    return (inp - inp.mean()) / inp.std()


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
mult = 1
for aa in a:
    mult = mult * aa

product_of_a = mult


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_in_a = [aa ** 2 for aa in a]
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [aa for aa in a if aa % 2 != 0]
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [aa for aa in a if aa % 2 == 0]
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

sum_of_b = sum(sum(b))


# Exercise 2 - refactor the following to use numpy.

min_of_b = np.amin(b)


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

max_of_b = np.amax(b)


# Exercise 4 - refactor the following using numpy to find the mean of b

mean_of_b = np.sum(b) / np.size(b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

product_of_b = np.prod(b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 

squares_of_b = b ** 2


# Exercise 7 - refactor using numpy to determine the odds_in_b

odds_in_b = len(sum(b % 2 != 0))


# Exercise 8 - refactor the following to use numpy to filter only the even numbers

evens_in_b = len(sum(b % 2 == 0))

# Exercise 9 - print out the shape of the array b.

print(b.shape)

# Exercise 10 - transpose the array b.

b = b.transpose()

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b = b.reshape(1, 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)


b = b.reshape(6, 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print(np.amin(c))
print(np.amax(c))
print(np.sum(c))
print(np.prod(c))
#print(np.asum(c)
# Exercise 2 - Determine the standard deviation of c.
print(np.std(c))
# Exercise 3 - Determine the variance of c.
print(np.var(c))
# Exercise 4 - Print out the shape of the array c
print(c.shape)
# Exercise 5 - Transpose c and print out transposed result.
c = c.transpose()
print(c.shape)
# Exercise 6 - Multiply c by the c-Transposed and print the result.
print(c * c.transpose())
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print(np.sum(c * c.transpose()))
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(np.product(c * c.transpose()))

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))
# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))
# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))
# Exercise 4 - Find all the negative numbers in d
print(len(d[d < 0]))
# Exercise 5 - Find all the positive numbers in d
print(len(d[d >= 0]))
# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))
# Exercise 7 - Determine how many unique numbers there are in d.
print(len(np.unique(d)))
# Exercise 8 - Print out the shape of d.
print(d.shape)
# Exercise 9 - Transpose and then print out the shape of d.
d = d.transpose()
print(d.shape)
# Exercise 10 - Reshape d into an array of 9 x 2
d = d.reshape(9, 2)
