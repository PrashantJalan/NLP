import codecs
import sys
import collections
import math
import re

#Importing my personalised modules
sys.path.append('./Functions/')
from sort_and_count import *
from print_func import *
from check import *


def main():
	if len(sys.argv)==1:
		file_path = 'Data.txt'
	else:
		file_path = argv[1]
		
	inp = open(file_path).read()
	inp = inp.decode("UTF-8")
	inp = inp.replace(',',' ')
	inp = inp.replace('.',' ')
	inp = inp.replace('\n',' ')
	inp = inp.replace('\t',' ')
	inp = inp.replace('<',' ')
	inp = inp.replace('>',' ')
	inp = inp.replace('-',' ')
	inp = inp.replace('(',' ')
	inp = inp.replace(')',' ')
	inp = inp.replace('{',' ')
	inp = inp.replace('}',' ')
	inp = inp.replace('[',' ')
	inp = inp.replace(']',' ')
	inp = inp.replace('"',' ')
	inp = inp.replace("'",' ')
	inp = inp.replace('?',' ')
	inp = inp.replace('`',' ')
	inp = inp.replace('!',' ')
	inp = inp.replace('*',' ')
	inp = inp.replace('$',' ')
	inp = inp.replace('@',' ')
	inp = inp.replace('#',' ')
	inp = inp.replace('%',' ')
	inp = inp.replace('^',' ')
	inp = inp.replace('&',' ')
	inp = inp.replace(';',' ')
	inp = inp.replace('/',' ')
	inp = inp.replace('\\',' ')
	inp = inp.replace('|',' ')
	inp = inp.replace('+',' ')
	inp = inp.replace('=',' ')
	inp = inp.replace('_',' ')
	inp = inp.replace('~',' ')

	word = inp.split()
	word = sort_count(word)
	print_func(word, 'Words.txt', len(word))
	

if __name__=='__main__':
	main()
