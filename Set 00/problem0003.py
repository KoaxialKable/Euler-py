#! /usr/bin/env python
############################################
#	Problem 3
#	Largest Prime Factor
#
#	The prime factors of 13195 are 5, 7, 13 and 29.
#	What is the largest prime factor of the number 600851475143 ?
#
#	Answer: 6857
############################################

# We're trying to find the prime factors of number
number = 600851475143

# isPrime takes integer n and returns True if it is prime
def isPrime(n):
	
	# iterate the value of n from 2 to n
	for i in range(2,n):
	
		# if any n is evenly divisible by any number, it's not prime
		if (n%i==0):
			return False
			
	# if not, it's prime
	return True

# findFactors finds ALL factors of integer n
def findFactors(n):

	# Prepare an empty list to hold all factors we find
	factors = []
	for i in range(2,n):
	
		# if i is greater than the square root of n, it's not a factor
		if i > (n ** (0.5)):
			break
			
		# if n is evenly divisible by i, it's a factor
		if (n%i==0):
			factors.append(i)
			factors.append(int(n/i))
		pass
		
	# sort the list in ascending order
	return sorted(factors)

# primeFactors identifies prime factors from the list 'factors'
def primeFactors(factors):

	#prepare an empty list to hold all the prime factors
	pf = []
	
	# iterate through elements of factors
	for v in factors:
		
		# if the factor is a prime factor, keep it in pf
		if(isPrime(v)):
			pf.append(v)
			
	#return list of prime factors
	return pf

# Print the last element resulting list of prime factors
print(primeFactors(findFactors(number))[-1])