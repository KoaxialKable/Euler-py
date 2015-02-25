#! /usr/bin/env python
############################################
#	Problem 6
#	Sum square difference
#
#	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#				a**2 + b**2 = c**2
#
#	For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
#	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#	Find the product abc.
#
#	Answer: 31875000 with 200, 375,  and 425
############################################
def solve():
	for a in range(2,334):
		for b in range(3,500):
			for c in range(4,501):
				if ((a+b+c) == 1000) and (a**2)+(b**2) == (c**2):
					print(a*b*c)
					#print(a,b,c)
					return
				pass
			pass
		pass
	pass

solve()