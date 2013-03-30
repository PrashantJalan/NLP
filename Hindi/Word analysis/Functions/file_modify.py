# This modify function just modifies a file string input into a desired list output format
import codecs

def file_modify(x):
	x = x.split('\t\t')
	i = 0
	while i<len(x):
		x[i] = x[i].strip()
		i = i+1
	x[0] = int(x[0])
	x[1] = int(x[1])
	if len(x)==3:
		x[2] = x[2].decode("UTF-8")
		x[2] = x[2].split()
	return x

def file_modify_freq(x):
	x = x.split()
	i = 0
	while i<len(x):
		x[i] = x[i].strip()
		i = i+1
	x[1] = float(x[1])
	x[0] = x[0].decode("UTF-8")
	return x
