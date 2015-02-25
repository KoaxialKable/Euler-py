#! /usr/bin/env python
############################################
#	Problem 6
#	Sum square difference
#
#	The sum of the squares of the first ten natural numbers is, 
#				1**2 + 2**2 + ... + 10**2 = 385
#
#	The square of the sum of the first ten natural numbers is,
#				(1 + 2 + ... + 10)**2 = 55**2 = 3025
#
#	Hence the difference between the sum of the squares of the first ten 
#		natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#	Find the difference between the sum of the squares of the first one 
#		hundred natural numbers and the square of the sum.
#
#	Answer: 25164150
############################################
def solveIt(n):
	sum1 = sum2 = 0
	#find the sum of individual integers 1 to n
	for i in range(1,n+1):
		sum1 += i**2
	
	# find the simple sum of integers 1 to n
	for i in range(1,n+1):
		sum2 += i	
	
	#return difference
	return sum2**2 - sum1
	
#print(solveIt(10))
print(solveIt(100))