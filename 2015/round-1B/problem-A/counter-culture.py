#!python
import sys


def expand(array, value, num, tested):
	reverseString = str(value)[::-1]
	reverse = int(reverseString)
	if reverse > value and reverse <= num:
		found = False
		if any(v == reverse for v in values):
			found = True
		if found == False:
			array.append(reverse)
	if value + 1 <= num:
		found = False
		if any(v == value + 1 for v in values):
			found = True
		if found == False:	
			array.append(value+1)


filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	num = int(f.readline())
	numReverse = int(str(num)[::-1])

	count = 0
	values = [0]
	tested = []

	while True:
		newArray = []
		for value in values:			
			expand(newArray, value, num, tested)
		values = newArray
		print values
		tested = tested + values
		count += 1
		if any(v == num for v in values):
			break

	print "Case #%d: %d" % (testcase, count)

f.close()