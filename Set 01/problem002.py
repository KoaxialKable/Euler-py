#! /usr/bin/env python
############################################
#	Problem 2
#	Even Fibonacci numbers
#
#	Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#	By starting with 1 and 2, the first 10 terms will be:
#						1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#		find the sum of the even-valued terms.
#
#	Answer: 4613732
############################################

# Initialize sum to 0, a to 1, and b to 2
# sum will hold the sum of even-values terms we find
# a and b are instruments to creating the Fibonacci series
sum,a,b = 0,1,2

# Create numbers in the Fibonacci sequence until the value of a passes 4,000,000
while (a <= 4000000):

	# Create Fibonacci series
	if (a%2==0):
	
		# Add the value of a to our sum
		sum += a
	
	# the new value of a becomes the old value of b
	# b becomes the sum of a and b, thus extending the Fibonacci series
	a,b = b,a+b
	
# Print resulting sum
print(sum)