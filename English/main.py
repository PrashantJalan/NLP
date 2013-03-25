import codecs
import sys
import collections
import math

#Importing my personalised modules
sys.path.append('./Functions/')
from file_modify import *
from sort_and_count import *
from print_func import *
from total_frame import *
from calc_pc import *

def main():
	if len(sys.argv)==1:
		file_path = 'Files/file.txt'
	else:
		file_path = argv[1]

	inp = open(file_path).readlines()
	inp = map(file_modify, inp)

	db_word = []							#Database of all the words built from the narrative corpus
	total_frame = calc_tf(inp, 1)
	video_frame = 598
	
	for item in inp:
		if len(item)==3:
			for it in item[2]:
				db_word.append(it)
	
	db_freq = sort_count(db_word)

	print_func(db_freq, 'Files/words.txt')

	pc = calc_pc1('Files/MR1.txt', video_frame)

if __name__=='__main__':
	main()
