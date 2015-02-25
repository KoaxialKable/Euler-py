#! /usr/bin/env python
############################################
#	Problem 1
#	Multiples of 3 and 5
#
#	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#	The sum of these multiples is 23.
#	Find the sum of all the multiples of 3 or 5 below 1000
#
#	Answer: 233168
############################################

# sum will hold the sum of all found multiples of 3 and 5
sum = 0

# Iterate the value of n from 1 to 999
for n in range(1,1000):
	
	# Check to see if n is divisible by 3 or 5
	if (n%3==0) or (n%5==0):
	
		# If yes, add n to sum
		sum += n
		
	pass
	
# Print resulting sum
print(sum)