#! /usr/bin/env python
############################################
#	Problem 5
#	Smallest multiple
#
#	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
#		without any remainder.
#
#	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
#	Answer: 232792560
############################################
def isPrime(n):
	for i in range(2,n):
		if (n%i==0):
			return False
	return True

def getBase(r):
	base = 1
	for i in range (1,r+1):
		if (isPrime(i)):
			base *= i
	return base

def findIt(n):
	foundIt = False
	guess = base = getBase(n)
	while not foundIt:
		for i in range(2,n+1):
			if(guess%i!=0):
				guess += base
				break
			if (i==n):
				return guess

#print(findIt(10))
#print(fintIt(30))
print('Answer:',findIt(20))

