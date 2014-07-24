#!python
import sys

filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	line = f.readline()
	inputs = line.split()
	C, F, X = map(float, inputs)

	rate = 2.0
	time = X/rate

	total_time = 0.0

	while True:
		time_if_buy = (C/rate) + X/(rate + F)
		if time_if_buy < time:	#buy farm
			total_time += C/rate
			rate += F
			new_time = total_time + X/rate
			if time > new_time:
				time = new_time
			else:
				break
		else:
			break

	print "Case #%d: %0.7f" % (testcase, time)

f.close()