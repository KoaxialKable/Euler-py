#! /usr/bin/env python
############################################
#	Problem 1
#	Number letter counts
#
#	If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
#	3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#	
#	If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#	how many letters would be used?
#
#	Answer: 21124 in 0.005 seconds
############################################
#	My first solution
import time

index   = [0,3,3,5,4,4,3,5,5,4]
teendex = [3,6,6,8,8,7,7,9,8,8]
tendex  = [0,3,6,6,5,5,5,7,6,6]

def convert(n):
	if len(str(n)) == 1:
		return index[n]
	elif len(str(n)) == 2:
		if n < 20:
			return teendex[n-10]
		else:
			return( tendex[int(str(n)[0])] + convert(int(str(n)[1])))
	elif len(str(n)) == 3:
		if n % 100 == 0:
			return index[int(str(n)[0])] + len('hundred')
		else:
			return index[int(str(n)[0])] + len('hundred') + len('and') + convert(int(str(n)[1::]))
	elif len(str(n)) == 4:
		return index[int(str(n)[0])] + len('thousand') + convert(int(str(n)[1::]))


start = time.time()
total = sum(convert(i) for i in range(1, 1001))
elapsed = time.time() - start

print('found {} in {} seconds'.format(total, elapsed))

