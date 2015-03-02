#! /usr/bin/env python
############################################
#	Problem 14
#	Longest Collatz sequence
#
#	The following iterative sequence is defined for the set of positive integers:
#	n → n/2 (n is even)
#	n → 3n + 1 (n is odd)
#
#	Using the rule above and starting with 13, we generate the following sequence: 
#			13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
#	It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#	Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#	Which starting number, under one million, produces the longest chain?
#
#	(NOTE: Once the chain starts the terms are allowed to go above one million.)
#
#	Answer: 837799
############################################
counter = []
number = 0
length = 0

def Collatz(num):
	counter.append(num)
	while num != 1:
		if num % 2 == 0:
			num = int(num / 2)
		else:
			num = 3*num + 1
		counter.append(num)
	counter.append(1)

for i in range (1, 1000000): # 1-13
	Collatz(i)
	if (len(counter) > length):
		length = len(counter)
		number = i
	counter = []
print('{}: {}'.format(number, length))