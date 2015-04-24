#!/usr/bin/env python3.4
import sys
import math


filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	f.readline()
	plates = sorted(map(int, list(
		f.readline().split())), reverse=True)
	max_ = plates[0]
	min_time = float('inf')

	for step in range (1, max_ + 1):
		move = 0
		for plate in plates:
			if plate <= step:
				break
			move += math.ceil(plate / step) - 1
		new_time = move + step
		if new_time < min_time:
			min_time = new_time
	print("Case #%d: %d" % (testcase, min_time))
	
f.close()
