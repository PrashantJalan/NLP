# Given a output filename and a list print_func will just print 
# the top 100 strings in the list, each string in a line if the list has only strings.
# Otherwise it will print the string and its frequency.
# It is meant for Hindi texts.

import codecs

def print_func(x, file_path, times):
	f = open(file_path, 'w')
	i = 0
	while i<times:
		if len(x[i])==1 or isinstance(x[i],basestring)==True :
			f.write(x[i].encode("UTF-8")+'\n')
		elif len(x[i])==2:
			f.write(x[i][0].encode("UTF-8")+' '+str(x[i][1])+'\n')
		else:
			print "Error! The output list to be printed has more than two attribute."
			quit()
		i = i+1

def print_func2(x, file_path, times):
	f = open(file_path, 'a')
	i = 0
	while i<times:
		if len(x[i])==2:
			f.write(x[i][0].encode("UTF-8")+'\n')
		else:
			print "Error! The output list to be printed has more than two attribute."
			quit()
		i = i+1

def print_func3(x, file_path, times):
	f = open(file_path, 'w')
	i = 0
	while i<times:
		if len(x[i])==2:
			f.write(x[i][0].encode("UTF-8")+'\n')
		else:
			print "Error! The output list to be printed has more than two attribute."
			quit()
		i = i+1
