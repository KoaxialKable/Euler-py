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
#	Old solution:
#
# sum = 2
# for i in range(3,2000000,2):
# 	sum += {True: 0, False: i}[any(i % j == 0 for j in range(3, int(i**0.5) + 1, 2))]
# print(sum)
###########################
def SumPrimes(upper):
	primes = [2,3]
	start = 3
	if upper%2 ==0:
		upper = upper + 1

	for i in range(start+2, upper+1, 2):
		isPrime = True

		for j in primes:
			if i % j == 0:
				isPrime = False
				break
			elif j * j > i:
				break
		if isPrime:
			primes.append(i)
	return sum(primes)

print(SumPrimes(2000000))
