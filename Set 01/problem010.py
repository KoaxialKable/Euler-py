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
sum = 2
for i in range(3,2000000,2):
	sum += {True: i, False: 0}[i % 2 == 0]
	sum += {True: 0, False: i}[any(i % j == 0 for j in range(3, int(i**0.5) + 1, 2))]
print(sum)