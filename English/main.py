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
from exclude_common import *
from calc_pl import *
from concept import *
from morphology import *
from combine import *
from ignore import *

def func_temp(x):
	return x[0]
	
def main():
	if len(sys.argv)==1:
		file_path = 'Files/file.txt'
	else:
		file_path = argv[1]

	inp = open(file_path).readlines()
	inp = map(file_modify, inp)

	# Instantiation
	db_word = []							#Database of all the words built from the narrative corpus
	total_frame = calc_tf(inp, 1)
	video_frame = 598
	
	
	for item in inp:
		if len(item)==3:
			for it in item[2]:
				db_word.append(it)
	
	#Remove the word inflections
	db_word = morphology(db_word)
	
	db_word = exclude(db_word)
	
	db_word = sort_count(db_word)
	
	# Ignore the words having frequency 1
	db_word = ignore_freq(db_word, 2)
		
	print_func(db_word, 'Files/words.txt')
	
	# Get the label probabilities of the labels in the db_word
	pl = calc_pl(db_word)
	print_func(pl,'Files/P(l).txt')

	#Database of label
	db = map(func_temp, db_word)

	# Concept association
	c1_filepath = 'Files/c1/MR.txt'
	c2_filepath = 'Files/c2/MR.txt'
	not_c1_filepath = 'Files/not_c1/MR.txt'
	not_c2_filepath = 'Files/not_c2/MR.txt'
	c1_combine_filepath = 'Files/comb_c1/'
	c2_combine_filepath = 'Files/comb_c2/'	
	
	concept(c1_filepath, total_frame, video_frame, db_word, db, pl)	
	concept(c2_filepath, total_frame, video_frame, db_word, db, pl)
	concept(not_c1_filepath, total_frame, video_frame, db_word, db, pl)
	concept(not_c2_filepath, total_frame, video_frame, db_word, db, pl)
	combine(c1_combine_filepath, c1_filepath.replace('MR.txt',''), not_c1_filepath.replace('MR.txt',''))
	combine(c2_combine_filepath, c2_filepath.replace('MR.txt',''), not_c2_filepath.replace('MR.txt',''))	


if __name__=='__main__':
	main()
