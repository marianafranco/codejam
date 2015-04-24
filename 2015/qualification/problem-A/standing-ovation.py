#!python
import sys


filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	line = f.readline()
	Smax, Sarray = line.split()
	Smax = int(Smax)
	Sarray = map(int, list(Sarray))

	count = 0
	result = 0
	for i, value in enumerate(Sarray):
		if count < i:
			friends = i - count
			result += friends
			count += friends
		count += value

	print "Case #%d: %d" % (testcase, result)
	
