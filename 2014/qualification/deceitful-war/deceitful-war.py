#!python
import sys

filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	num_blocks = int(f.readline())

	naomi = []
	ken = []

	line = f.readline()
	naomi = map(float, line.split())
	line = f.readline()
	ken= map(float, line.split())

	naomi_blocks = sorted(naomi)
	ken_blocks = sorted(ken)

	#print naomi_blocks
	#print ken_blocks

	# deceitful war
	p_naomi = 0
	naomi = naomi_blocks[:]
	ken = ken_blocks[:]
	while len(naomi) != 0:
		if ken[-1] > naomi[-1]:
			del ken[-1]
			del naomi[0]
		else:
			for b in naomi:
				if b > ken[0]:
					p_naomi += 1
					del b
					del ken[0]
			break

	# normal war
	p_naomi_war = 0
	naomi = naomi_blocks[:]
	ken = ken_blocks[:]
	while len(naomi) != 0:
		ken_greater_blocks = [i for i in ken if i >= naomi[-1]]
		#print ken_greater_blocks
		if len(ken_greater_blocks) != 0:
			ken_greater_blocks = sorted(ken_greater_blocks)
			del naomi[-1]
			ken.remove(ken_greater_blocks[-1])
		else:
			p_naomi_war += 1
			del naomi[-1]
			del ken[0]

	print "Case #%d: %d %d" % (testcase, p_naomi, p_naomi_war)

f.close()