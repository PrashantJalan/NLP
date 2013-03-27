# Given a output filename and a list print_func will just print 
# all the strings in the list, each string in a line if the list has only strings.
# Otherwise it will print the string and its frequency.
# It is meant for Hindi texts.

import codecs

def print_func(x, file_path):
	f = open(file_path, 'w')
	i = 0
	while i<len(x):
		if len(x[i])==1 or isinstance(x[i],basestring)==True :
			f.write(x[i].encode("UTF-8")+'\n')
		elif len(x[i])==2:
			f.write(x[i][0].encode("UTF-8")+' '+str(x[i][1])+'\n')
		else:
			print "Error! The output list to be printed has more than two attribute."
			quit()
		i = i+1
		
def print_file(x, file_path):
	f = open(file_path, 'w')
	i = 0
	while i<len(x):
		f.write(str(x[i][0])+'\t\t'+str(x[i][1])+'\t\t')
		if len(x[i])==3:
			for item in x[i][2]:
				f.write(item.encode("UTF-8")+' ')
		f.write('\n')
		i = i+1
