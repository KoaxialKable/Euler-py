#! /usr/bin/env python
############################################
#	Problem 456
#	Triangles containing the origin II
#
#	Define:
#	x(n) = (1248^n mod 32323) - 16161
#	y(n) = (8421^n mod 30103) - 15051
#	P(n) = {(x1, y1), (x2, y2), ..., (xn, yn)}
#
#	For example, P(8) = {(-14913, -6630), (-10161, 5625), (5226, 11896), (8340, -10778), 
#					  (15852, -5203), (-15165, 11295), (-1427, -14495), (12407, 1060)}.
#
#	Let C(n) be the number of triangles whose vertices are in P(n) which contain the origin in the interior.
#
#	Examples:
#	C(8) = 20
#	C(600) = 8950634
#	C(40 000) = 2666610948988
#
#	Find C(2 000 000)
#
#	Answer: 
############################################
points_list = []

def getPoints(count):
	origin_counter = 0
	x = 1
	y = 1

	print('Processing...')
	for i in range(0, count):
		x = x*1248%32323
		y = y*8421%30103
		px = x - 16161
		py = y - 15051
		if px == 0 and py == 0:
			origin_counter = origin_counter + 1
		point = {'x': px, 'y': py}
		points_list.append(point)
	print('Done.')
	# for p in points_list:
	# 	print('({}, {})'.format(p['x'], p['y']))

getPoints(2000000)