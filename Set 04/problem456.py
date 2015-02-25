#! /usr/bin/env python
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