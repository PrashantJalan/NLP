# This python code simply retrieves a file stores it syllables and k-grams.
# For Hindi text.
# Calculates the total frames (sum of all the frames). The total frames in all the video may not be the same.
# It also makes a main narrative corpus (based on the input files) and stores their frequent syllables and k-grams

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
from syllable import *
from kgrams import *


def main():
	if len(sys.argv)==1:
		file_path = 'Files/file.txt'
	else:
		file_path = argv[1]

	inp = open(file_path).readlines()
	inp = map(file_modify, inp)

	#Instantiation
	total_frame = calc_tf(inp, 1)
	video_frame = 598
	type_of_kgram = ['2','3','4','5','6']
	
	#Processing
	pc = calc_pc1('Files/MR1.txt', video_frame)

if __name__=='__main__':
	main()
