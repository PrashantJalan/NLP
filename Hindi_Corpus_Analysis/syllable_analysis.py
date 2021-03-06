import codecs
import sys
import collections
import math

#Importing my personalised modules
sys.path.append('./Functions/')
from sort_and_count import *
from print_func import *
from kgrams import *
from syllable import *

def my_sort(x):
	return x[-1]


def main():
	if len(sys.argv)==1:
		file_path = 'Data.txt'
	else:
		file_path = argv[1]

	inp = open(file_path).read()
	inp = inp.decode("UTF-8")
	inp = list(inp)

	# Get the most frequent syllables
	syllable = get_syll(inp)
	print "Computed syllables"

	# Get the most frequent k-grams
	kgram = kgrams(syllable, ['2'])
	kgram_freq = sort_count(kgram)
	comb = kgram_freq[0:1000]
	print_func(kgram_freq,'Top50/gram2.txt',50)
	print_func(kgram_freq,'Top100/gram2.txt',100)
	print_func(kgram_freq,'Top200/gram2.txt',200)
	print_func(kgram_freq,'Top300/gram2.txt',300)
	print_func(kgram_freq,'Top500/gram2.txt',500)
	print_func(kgram_freq,'Top1000/gram2.txt',1000)
	print "Computed gram2"
	
	kgram = kgrams(syllable, ['3'])
	kgram_freq = sort_count(kgram)
	comb = kgram_freq[0:1000] + comb
	print_func(kgram_freq,'Top50/gram3.txt', 50)
	print_func(kgram_freq,'Top100/gram3.txt', 100)
	print_func(kgram_freq,'Top200/gram3.txt',200)
	print_func(kgram_freq,'Top300/gram3.txt',300)
	print_func(kgram_freq,'Top500/gram3.txt',500)
	print_func(kgram_freq,'Top1000/gram3.txt',1000)
	print "Computed gram3"
	
	kgram = kgrams(syllable, ['4'])
	kgram_freq = sort_count(kgram)
	comb = kgram_freq[0:1000] + comb
	print_func(kgram_freq,'Top50/gram4.txt', 50)
	print_func(kgram_freq,'Top100/gram4.txt', 100)
	print_func(kgram_freq,'Top200/gram4.txt',200)
	print_func(kgram_freq,'Top300/gram4.txt',300)
	print_func(kgram_freq,'Top500/gram4.txt',500)
	print_func(kgram_freq,'Top1000/gram4.txt',1000)
	print "Computed gram4"

	kgram = kgrams(syllable, ['5'])
	kgram_freq = sort_count(kgram)
	comb = kgram_freq[0:1000] + comb
	print_func(kgram_freq,'Top50/gram5.txt', 50)
	print_func(kgram_freq,'Top100/gram5.txt', 100)
	print_func(kgram_freq,'Top200/gram5.txt',200)
	print_func(kgram_freq,'Top300/gram5.txt',300)
	print_func(kgram_freq,'Top500/gram5.txt',500)
	print_func(kgram_freq,'Top1000/gram5.txt',1000)
	print "Computed gram5"
	
	kgram = kgrams(syllable, ['6'])
	kgram_freq = sort_count(kgram)
	comb = kgram_freq[0:1000] + comb
	print_func(kgram_freq,'Top50/gram6.txt', 50)
	print_func(kgram_freq,'Top100/gram6.txt', 100)
	print_func(kgram_freq,'Top200/gram6.txt',200)
	print_func(kgram_freq,'Top300/gram6.txt',300)
	print_func(kgram_freq,'Top500/gram6.txt',500)
	print_func(kgram_freq,'Top1000/gram6.txt',1000)
	print "Computed gram6"
	
	comb.sort(key=my_sort, reverse=True)
	print_func(comb,'Top50/comb.txt', 50)
	print_func(comb,'Top100/comb.txt', 100)
	print_func(comb,'Top200/comb.txt',200)
	print_func(comb,'Top300/comb.txt',300)
	print_func(comb,'Top500/comb.txt',500)
	print_func(comb,'Top1000/comb.txt',1000)
	print "Calculated combination of all"
	

if __name__=='__main__':
	main()
