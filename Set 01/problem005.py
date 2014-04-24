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
#	Answer: 
############################################
n = 400
while True:
	for i in range(2,21):
		if (n%i!=0):
			n += 1
			continue
	if (i == 21)
		break

print(n)