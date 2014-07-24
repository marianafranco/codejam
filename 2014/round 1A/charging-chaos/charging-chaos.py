#!python
import sys

def to_list(x):
	return list(x)

def matches(flow, desired):
	return sorted(flow) == sorted(desired)

def flip(n, elements):
  output = []
  for i in elements:
  	i = [k for k in i]
  	if i[n] == '1':
  		i[n] = '0'
  	else:
  		i[n] = '1'
  	output.append(''.join(i))
  return output

def compare_n_element_old(n, initial, desired):
	initial_n_elements = []
	for i in initial:
		elements = list(i)
		initial_n_elements.append(''.join(elements[0:n+1]))
	desired_n_element = []
	for i in desired:
		elements = list(i)
		desired_n_element.append(''.join(elements[0:n+1]))
	#print initial_n_elements
	#print desired_n_element
	#print sorted(initial_n_elements) == sorted(desired_n_element)
	return sorted(initial_n_elements) == sorted(desired_n_element)

def compare_n_element(n, initial, desired):
	return sorted([i[:n+1] for i in initial]) == sorted([i[:n+1] for i in desired])

def recursive(count, index, initial, desired):
	if index == len(desired[0]):
		return	# not found
	if matches(initial, desired):
		return count
	else:
		if compare_n_element(index, initial, desired):
			result = recursive(count, index+1, initial, desired)
			if result is not None:
				return result

		flipped = flip(index, initial)
		if matches(flipped, desired):
			count+=1
			return count
		else:
			if compare_n_element(index, flipped, desired):
				return recursive(count+1, index+1, flipped, desired)
			else:
				return

filename = sys.argv[1]
f = open(filename, 'r')

# number of testcases
T = int(f.readline())

for testcase in range(1,T+1):
	line = f.readline()
	N, L = map(int, line.split())

	first_line = f.readline()
	#initial_flow = map(to_list, first_line.split())
	initial_flow = first_line.split()

	second_line = f.readline()
	#desired_flow = map(to_list, second_line.split())
	desired_flow = second_line.split()

	result = recursive(0,0,initial_flow, desired_flow)

	if result is not None:
		print "Case #%d: %d" % (testcase, result)
	else:
		print "Case #%d: NOT POSSIBLE" % (testcase)

f.close()	