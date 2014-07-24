#!python
import sys

filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	first_answer = int(f.readline())
	for row in range(1,5):
		line = f.readline()
		if row == first_answer:
			first_row_line = line
	first_row = first_row_line.split()

	second_answer = int(f.readline())
	for row in range(1, 5):
		line = f.readline()
		if row == second_answer:
			second_row_line = line
	second_row = second_row_line.split()

	#print first_row
	#print second_row

	result = set(first_row).intersection(set(second_row))
	#print result

	length = len(result)
	if length == 0:
		print "Case #%d: Volunteer cheated!" % (testcase)
	elif length == 1:
		print "Case #%d: %s" % (testcase, result.pop())
	else:
		print "Case #%d: Bad magician!" % (testcase)
f.close()