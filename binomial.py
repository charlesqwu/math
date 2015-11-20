# This set of solutions is for calculating the binomial coefficient C(n,k)

# These code snippets have been tested in Python2.7
# To test in Python3.x, just need to change print statement to print function

# Solution 1: Use the beta() function in the scipy.special module
# The beta() function is basically an analytic extension of the binomial
# function from non-negative integers to complex numbers
from scipy.special import beta
def c(n, k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k
    return int(1/((n+1) * beta(n-k+1, k+1)))


# Solution 2: Use the convolve() function in the numpy module
# The discrete convolution between two vectors corresponds to multiplying
# the two polynomials with coefficients as the two vectors
from numpy import convolve
def c(n, k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k

    if n < 2: return 1
    kernel, row = [1,1], [1]
    for i in range(n):
        row = convolve(kernel, row)
    return row[k]


# Solution 3: Use the polymul() function from the numpy.polynomial module
# basically the same kind of solution as the above one
from numpy.polynomial import polymul
def c(n, k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k

    if n < 2: return 1
    kernel, row = [1,1], [1]
    for i in range(n):
        row = polymul(kernel, row)
    return int(row[k])


# Solution 4: Use the factorial() function from the math module
from math import factorial
def c(n,k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k
    return factorial(n) / (factorial(n-k) * factorial(k))

# or gamma
from math import gamma
def c(n,k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k
    return int(gamma(n+1) / (gamma(n-k+1) * gamma(k+1)))

# Solution 5:
# define a function for falling factorial (aka, Pochhammer notation)
# falling-factorial(n,k) = n*(n-1)*......*(n-k+1)
def ff(n, k):
    return reduce(lambda p,i:p*i, range(n,k,-1), 1)

def c(n, k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k
    return ff(n, n-k) / ff(k, 1)


# Solution 6: recursive solution
def b(n, k):
    if n < 0 or k > n: 
        return 0
    if k==0 or k==n: 
        return 1
    if k > n/2: 
        k = n - k
    return b(n-1,k-1) + b(n-1,k)


# Solution 7: iterative (dynamic programming)
def c(n, k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k

    p=[1]
    for i in range(1, n+1):
        new = 1
        for j in range(1, i):
            new, p[j-1] = p[j-1] + p[j], new
        p[-1:] = new, 1
    return p[k]


# Solution 8: generate numbers in 0...2^n, and count bits in them
# c(n,k) = the count of numbers with k bits = 1
# This algorithm is certainly slow with time complexity O(2^n) --
# it is listed here just as a possible solution
def c(n, k):
    if n < 0 or k > n: return 0
    if k > n/2: k = n - k
    
    """
    count=0
    for i in range(pow(2,n)):
        if bin(i).count('1') == k:
            count+=1
    return count
    """
    # the line below just implements the above loop using functional programming
    return reduce(lambda c,i:c+1 if bin(i).count('1') == k else c, range(pow(2,n)), 0)

# Solution 9: generate a binomial distribution
from random import random
def toss(n, k):
    # print n, k
    count=0
    for i in range(n):
        if random() <= 0.5:
            count += 1
            # print count
    return 1 if count==k else 0

def c(n, k):
    samples = 1000000
    counts = 0
    for i in range(samples):
        counts += toss(n,k)
    # print counts
    return int(round(counts * pow(2,n) * 1.0 / samples))

# test - print the PASCAL triangle with 20 rows
for i in range(20):
    for j in range(i+1):
        print c(i, j),
    print


