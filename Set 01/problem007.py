#! /usr/bin/env python
############################################
#	Problem 7
#	10001st prime
#
#	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#	What is the 10,001st prime number?
#
#	Answer: 104743
############################################
def isPrime(n):
	if (n==2):
		return True
	if (n < 2) or (n % 2 == 0):
		return False
	
	# any() returns True if any element of the iterable is true and false if it is false
	# here, if (n % i == 0) [true], indicating evenly divisible and thus not prime,
	# the result will be false.  It iterates between 3 and the integer form of the square root
	# of n, because if it's not divisible by any number smaller than its own square root, it's prime.
	# It only evaluates odd numbers because we already checked for divisibility by 2, above.
	return not any(n % i == 0 for i in range(3,int(n**0.5) + 1, 2))

def nthPrime(n):
	if (n==1):
		return 2
	count, i = 0, 2
	primes = []
	while (count < n):
		#outer counting loop 1..n looking for primes
		if (isPrime(i)):
			primes.append(i)
			count += 1
		i += 1 
	return primes[-1]

#print(nthPrime(1))
#print(nthPrime(2))
#print(nthPrime(6))
print(nthPrime(10001))