#! /usr/bin/env python
############################################
#	Problem 3
#	Largest Prime Factor
#
#	The prime factors of 13195 are 5, 7, 13 and 29.
#	What is the largest prime factor of the number 600851475143 ?
#
############################################
number = 600851475143
def isPrime(n):
	for i in range(2,n):
		if (n%i==0):
			return False
	return True

def findFactors(n):
	factors = []
	for i in range(2,n):
		if i > (n ** (0.5)):
			break
		if (n%i==0):
			factors.append(i)
			factors.append(int(n/i))
	return sorted(factors)

def primeFactors(factors):
	pf = []
	for v in factors:
		if(isPrime(v)):
			pf.append(v)
	return pf

print(primeFactors(findFactors(number))[-1])

