#! /usr/bin/env python
############################################
#	Problem 16
#	Power digit sum
#
#	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#	
#	What is the sum of the digits of the number 2^1000?
#
#	Answer: 
############################################
sum = 0
for char in str(2**1000):
	sum += int(char)
print(sum)