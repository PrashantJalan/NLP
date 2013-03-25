# Given a list this function counts the no. of occurences of a particular
# key and sorts it accordingly in the decreasing manner.

import collections

def sort_count(x):
	counter = collections.Counter(x)
	X = []
	Y = []
	for (y,x) in sorted(zip(counter.values(),counter.keys()), reverse=True):
		X.append(x)
		Y.append(y)
	return zip(X,Y)
