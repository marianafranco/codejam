#!python
import sys


filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	num = int(f.readline())
	numReverse = int(str(num)[::-1])

	actual = 0
	count = 0
	
	while actual != num:
		reverseString = str(actual)[::-1]
		reverse = int(reverseString)
		
		if reverse > actual and reverse <= num:
			if numReverse < num and actual < numReverse:
				diff1 = numReverse - actual
			else:
				diff1 = num - actual
			
			diff2 = num - reverse

			if diff1 < diff2:
				actual+=1
			else:	
				actual = reverse
		else:
			actual+=1
		count+=1
		print actual

	print "Case #%d: %d" % (testcase, count)


f.close()