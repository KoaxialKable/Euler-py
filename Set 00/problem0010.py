#! /usr/bin/env python
############################################
#	Problem 10
#	summation of primes
#
#	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#	Find the sum of all the primes below two million.
#
#	Answer: 142913828922
############################################
#	My actual, inferior solution:
#
# sum = 2
# for i in range(3,2000000,2):
# 	sum += {True: 0, False: i}[any(i % j == 0 for j in range(3, int(i**0.5) + 1, 2))]
# print(sum)
###########################
import time
 
def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2 	
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum
 
start = time.time()
sum = prime_sum(2000000)
elapsed = (time.time() - start)
 
print ('found %s in %s seconds' % (sum,elapsed))
# This solution was shamelessly stolen and copied from "Jason's Code Blog" at http://code.jasonbhill.com/sage/project-euler-problem-10/
# Thanks, Jason!