#This function is written for label association of a label with a given concept
# A concept is identified by the MR.txt file
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
from kgrams import *
from exclude_common import *
from calc_pl import *
from involvement import *

threshold = 0.75

def mysort(x):
	return x[-1]

def concept(path, total_frame, video_frame, inp, label, pl):
	
	def_path = path.replace('MR.txt','')
	
	original = open('Files/file.txt').readlines()
	original = map(file_modify, original)
	
	mr = open(path).readlines()
	mr = map(file_modify, mr)

	# Get the probability of concept 1 happening 
	pc = calc_pc1(path, video_frame)

	# Get thhe concept.txt file
	i = len(inp)-1
	while i>=0:
		flag = 0
		if len(inp[i])==3:
			for it in mr:
				if involved(it, [inp[i][0],inp[i][1]]) > threshold:
					flag = 1
					break
		if flag==0:
			original.pop(i)
			inp.pop(i)
		i = i-1
	
	print_file(original, def_path+'concept.txt')

	# Joint probability of the concept and the label happening together
	jp = []
	for item in label:
		temp = 0.0
		for it in inp:
			if len(it)==3:
				if item in it[2]:
					temp = temp + it[1] - it[0]
		jp.append([item, temp/total_frame])
	
	# Mutual information
	mi = []
	i = 0
	for item in jp:
		if item[1]!=0:
			temp = float(item[1]) * math.log((item[1] / (pc * pl[i][1])), 2)
			mi.append([item[0],temp])
		i = i+1

	jp.sort(key=mysort, reverse=True)
	print_func(jp, def_path+'jp.txt')
	
	mi.sort(key=mysort, reverse=True)
	print_func(mi, def_path+'mi.txt')


if __name__=='__main__':
	main()
