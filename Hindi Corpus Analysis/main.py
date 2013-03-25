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
from sort_and_count import *
from print_func import *
from syllable import *
from kgrams import *


def main():
	if len(sys.argv)==1:
		file_path = 'Data.txt'
	else:
		file_path = argv[1]

	inp = open(file_path).read()
	inp = inp.decode("UTF-8")
	inp = list(inp)

	# Get the most frequent syllables
	syllable = get_syll(inp, 0)

	print_func (syllable, 'test.txt')
	syllable_freq = sort_count(syllable)
	print_func(syllable_freq,'gram1.txt')
	print "Computed gram1"

	# Get the most frequent k-grams
	kgram = kgrams(syllable, ['2'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'gram2.txt')
	print "Computed gram2"
	
	kgram = kgrams(syllable, ['3'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'gram3.txt')
	print "Computed gram3"
	
	kgram = kgrams(syllable, ['4'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'gram4.txt')
	print "Computed gram4"

	kgram = kgrams(syllable, ['5'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'gram5.txt')
	print "Computed gram5"
	
	kgram = kgrams(syllable, ['6'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'gram6.txt')
	print "Computed gram6"

if __name__=='__main__':
	main()
