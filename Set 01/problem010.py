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
def isPrime(n):
	if (n==2):
		return True
	if (n < 2) or (n % 2 == 0):
		return False
	return not any(n % i == 0 for i in range(3,int(n**0.5) + 1, 2))

for i in range(3,2000000,2):
	# ternary expression.  if prime, add i to sum. if not, add 0
	sum += {True: i, False: 0}[isPrime(i)]
	
print(sum)