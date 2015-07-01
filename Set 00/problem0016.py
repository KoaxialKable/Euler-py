#! /usr/bin/env python
############################################
#	Problem 16
#	Power digit sum
#
#	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#	
#	What is the sum of the digits of the number 2^1000?
#
#	Answer: 1366
############################################
#	My first solution
#
# total = 0
# for char in str(2**1000):
# 	total += int(char)
# print(total)
############################################
#	More pythonic solution
print(sum(int(digit) for digit in str(2**1000)))