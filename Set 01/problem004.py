#! /usr/bin/env python
############################################
#	Problem 4
#	Largest palindrome product
#
#	A palindromic number reads the same both ways.
#	The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#	Find the largest palindrome made from the product of two 3-digit numbers.
#
############################################
pals = []
def isPalindrome(n):
	if (str(n) == str(n)[::-1]):
		return True
	return False
	
for i in range(999,99,-1):
	for j in range(999,99,-1):
			if(isPalindrome(i*j)):
				pals.append(i*j)
				
print(sorted(pals)[-1])