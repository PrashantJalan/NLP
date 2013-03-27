import codecs
import sys
import collections
import math

#Importing my personalised modules
sys.path.append('./Functions/')
from sort_and_count import *
from print_func import *
from kgrams import *

#We couldn't use our syllable function because that is quite slow
def extractor(text):	
#Func to extract syllables
#Takes a list of characters without spaces as input

	syllable=[]
	i=0
	while i<len(text):
		if text[i]>=u'\u0904' and text[i]<=u'\u0914':
			#Scan a vowel
			syllable.append(text[i])
			if (i+1)<len(text):
				if text[i+1]>=u'\u0900' and text[i+1]<=u'\u0903':
					#Scans a special sybmol
					temp = ''.join([syllable.pop(),text[i+1]])
					syllable.append(temp)
					i=i+1
			
		elif (text[i]>=u'\u0915' and text[i]<=u'\u0939') or (text[i]>=u'\u0958' and text[i]<=u'\u095F'):
			#Scans a consonent
			syllable.append(text[i])
			i=i+1
			while i<len(text):
				if text[i]>=u'\u0915' and text[i]<=u'\u0939':
					#Scans a consonent
					i=i-1	#Ignore it
					break
				elif (text[i]>=u'\u0958' and text[i]<=u'\u095F'):
					#Scans a special consonent
					i=i-1	#Ignore it
					break
				elif text[i]>=u'\u0904' and text[i]<=u'\u0914':
					#Scans a vowel
					i=i-1	#Ignore it
					break
				elif text[i]==u'\u094D':
					#Scans a halant
					temp = ''.join([syllable.pop(),text[i],text[i+1]])	#Take another character
					syllable.append(temp)
					i=i+2
				elif text[i]>=u'\u0900' and text[i]<=u'\u0903':
					#Scans a special sybmol
					temp = ''.join([syllable.pop(),text[i]])
					syllable.append(temp)
					i=i+1
				elif text[i]>=u'\u093E' and text[i]<=u'\u094C':
					#Scans a matra
					temp = ''.join([syllable.pop(),text[i]])
					syllable.append(temp)
					i=i+1
				elif text[i]=='\n' or text[i]==' ' or text[i]==u'\x85':
					i=i+1
				else:
					#Scans something else
					i=i+1

		else:
			pass

		i=i+1
		
	return syllable
	

def main():
	if len(sys.argv)==1:
		file_path = 'Data.txt'
	else:
		file_path = argv[1]

	inp = open(file_path).read()
	inp = inp.decode("UTF-8")
	inp = list(inp)

	# Get the most frequent syllables
	syllable = extractor(inp)
	print "Computed syllables"

	# Get the most frequent k-grams
	kgram = kgrams(syllable, ['2'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'Top50/gram2.txt',50)
	print_func(kgram_freq,'Top100/gram2.txt',100)
	print_func(kgram_freq,'Top200/gram2.txt',200)
	print_func(kgram_freq,'Top300/gram2.txt',300)
	print_func(kgram_freq,'Top500/gram2.txt',500)
	print_func(kgram_freq,'Top1000/gram2.txt',1000)
	print_func3(kgram_freq,'Top50/comb.txt',50)
	print_func3(kgram_freq,'Top100/comb.txt',100)
	print_func3(kgram_freq,'Top200/comb.txt',200)
	print_func3(kgram_freq,'Top300/comb.txt',300)
	print_func3(kgram_freq,'Top500/comb.txt',500)
	print_func3(kgram_freq,'Top1000/comb.txt',1000)	
	print "Computed gram2"
	
	kgram = kgrams(syllable, ['3'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'Top50/gram3.txt', 50)
	print_func(kgram_freq,'Top100/gram3.txt', 100)
	print_func(kgram_freq,'Top200/gram3.txt',200)
	print_func(kgram_freq,'Top300/gram3.txt',300)
	print_func(kgram_freq,'Top500/gram3.txt',500)
	print_func(kgram_freq,'Top1000/gram3.txt',1000)
	print_func2(kgram_freq,'Top50/comb.txt',50)
	print_func2(kgram_freq,'Top100/comb.txt',100)
	print_func2(kgram_freq,'Top200/comb.txt',200)
	print_func2(kgram_freq,'Top300/comb.txt',300)
	print_func2(kgram_freq,'Top500/comb.txt',500)
	print_func2(kgram_freq,'Top1000/comb.txt',1000)	
	print "Computed gram3"
	
	kgram = kgrams(syllable, ['4'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'Top50/gram4.txt', 50)
	print_func(kgram_freq,'Top100/gram4.txt', 100)
	print_func(kgram_freq,'Top200/gram4.txt',200)
	print_func(kgram_freq,'Top300/gram4.txt',300)
	print_func(kgram_freq,'Top500/gram4.txt',500)
	print_func(kgram_freq,'Top1000/gram4.txt',1000)
	print_func2(kgram_freq,'Top50/comb.txt',50)
	print_func2(kgram_freq,'Top100/comb.txt',100)
	print_func2(kgram_freq,'Top200/comb.txt',200)
	print_func2(kgram_freq,'Top300/comb.txt',300)
	print_func2(kgram_freq,'Top500/comb.txt',500)
	print_func2(kgram_freq,'Top1000/comb.txt',1000)	
	print "Computed gram4"

	kgram = kgrams(syllable, ['5'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'Top50/gram5.txt', 50)
	print_func(kgram_freq,'Top100/gram5.txt', 100)
	print_func(kgram_freq,'Top200/gram5.txt',200)
	print_func(kgram_freq,'Top300/gram5.txt',300)
	print_func(kgram_freq,'Top500/gram5.txt',500)
	print_func(kgram_freq,'Top1000/gram5.txt',1000)
	print_func2(kgram_freq,'Top50/comb.txt',50)
	print_func2(kgram_freq,'Top100/comb.txt',100)
	print_func2(kgram_freq,'Top200/comb.txt',200)
	print_func2(kgram_freq,'Top300/comb.txt',300)
	print_func2(kgram_freq,'Top500/comb.txt',500)
	print_func2(kgram_freq,'Top1000/comb.txt',1000)	
	print "Computed gram5"
	
	kgram = kgrams(syllable, ['6'])
	kgram_freq = sort_count(kgram)
	print_func(kgram_freq,'Top50/gram6.txt', 50)
	print_func(kgram_freq,'Top100/gram6.txt', 100)
	print_func(kgram_freq,'Top200/gram6.txt',200)
	print_func(kgram_freq,'Top300/gram6.txt',300)
	print_func(kgram_freq,'Top500/gram6.txt',500)
	print_func(kgram_freq,'Top1000/gram6.txt',1000)
	print_func2(kgram_freq,'Top50/comb.txt',50)
	print_func2(kgram_freq,'Top100/comb.txt',100)
	print_func2(kgram_freq,'Top200/comb.txt',200)
	print_func2(kgram_freq,'Top300/comb.txt',300)
	print_func2(kgram_freq,'Top500/comb.txt',500)
	print_func2(kgram_freq,'Top1000/comb.txt',1000)	
	print "Computed gram6"

if __name__=='__main__':
	main()
