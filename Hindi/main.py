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
from calc_pl import *
from exclude_common import *
from merge_common import *


def main():
	
	if len(sys.argv)==1:
		file_path = 'Files/file.txt'
	else:
		file_path = argv[1]

	inp = open(file_path).readlines()
	inp = map(file_modify, inp)

	# Instantiation
	total_frame = calc_tf(inp, 1)
	video_frame = 598
	type_of_kgram = ['2','3','4','5','6']
	
	# Processing the main file
	
	# Get the syllables and kgrams of the main file
	# kgram will contain all the labels that we need to associate with the concept
	# inp will contain the information in the format [initial frame, final frame, [labels]]
	syllable = []
	kgram = []
	
	i = 0
	while i<len(inp):
		if len(inp[i])==3:
			temp = get_syll(inp[i][2],1)
			syllable = syllable + temp
			tmp = kgrams(temp, type_of_kgram)
			kgram = kgram + tmp
			inp[i][2] = kgram
		i = i+1

	syllable = sort_count(syllable)
	print_func(syllable,'Files/syllable.txt')

	print_file(inp, 'Files/input.txt')
	
#	kgram_temp = sort_count(kgram)
#	print_func(kgram_temp, 'Files/kgram_without_exclusion.txt')
	
	# Throw away the common kgrams
#	kgram = exclude(kgram)

	#Sort and count
	kgram = sort_count(kgram)
#	print_func(kgram, 'Files/kgram_without_merging.txt')

	# You may try merging the smaller ones into bigger ones here to get better results	
#	kgram = merge_same(kgram)

	# Ignore the kgrams having frequency 1
	i = len(kgram)-1
	while i>=0:
		if kgram[i][1]==1:
			kgram.pop(i)
		i = i-1
	
	print_func(kgram,'Files/kgram.txt')	
	
	# Get the label probabilities of the labels in the kgram
	pl = calc_pl(kgram)
	print_func(pl,'Files/P(l).txt')


	# Get the concept 1 file
	
	# Get the syllables of concept 1 file
	
	# Get the k-grams of concept 1 file
	
	# Get the probability of concept 1 happening 
	pc = calc_pc1('Files/MR2.txt', video_frame)
	print pc

if __name__=='__main__':
	main()
