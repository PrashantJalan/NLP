# Makes the not_MR.txt of a given MR
#Importing my personalised modules

import sys

sys.path.append('./Functions/')
from file_modify import *

def not_MR(filepath):
	
	mr = open(filepath).readlines()
	mr = map(file_modify, mr)

	new_path = filepath.replace('MR.txt', 'not_MR.txt')
	
	f = open(new_path, 'w')
	
	not_mr = []
	prev = 0
	for item in mr:
		if item[0]!=prev+1:
			tmp1 = prev+1
			tmp2 = item[0]-1
			if tmp2>tmp1:
				not_mr.append([tmp1,tmp2])
		prev = item[1]
		
	for item in not_mr:
		f.write(str(item[0])+'\t\t'+str(item[1])+'\n')
	f.close()
