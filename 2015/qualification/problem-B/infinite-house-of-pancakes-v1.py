#!python
import sys


filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

def expand_array(s_array):
	step = max(s_array)
	position = s_array.index(step)
	a = s_array[position] / 2
	b = s_array[position] - a
	s_array[position] = a 
	s_array = s_array + [b]
	return s_array

for testcase in range(1,T+1):
	f.readline()
	Sarray = map(int, list(
		f.readline().split()))

	minutes = 0

	step = max(Sarray)
	
	Sarray = expand_array(Sarray)
	minutes = minutes + 1
	new_step = max(Sarray) + minutes
	 
	while max(Sarray) != 1:
		if new_step < step:
			step = new_step 
		
		Sarray = expand_array(Sarray)
		minutes = minutes + 1
		new_step = max(Sarray) + minutes
		
	print "Case #%d: %d" % (testcase, step)
	
