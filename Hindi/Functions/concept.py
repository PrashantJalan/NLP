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
from calc_pc import *
from involvement import *
from morphology import *
from exclude_common import *
from merge_common import *
from shift_frame import *

threshold = 0.9

def mysort(x):
	return x[-1]

def concept(path, total_frame, video_frame, kgram_main, label, pl):
	
	def_path = path.replace('MR.txt','')
	
	original = open('Files/file.txt').readlines()
	original = map(file_modify2, original)
	inp = open('Files/input.txt').readlines()
	inp = map(file_modify2, inp)
	
	mr = open(path).readlines()
	mr = map(file_modify, mr)
	
	# Shift the frames to account for the verbal delay
#	mr = shift_frame(mr, 10)

	# Get the probability of concept 1 happening 
	pc = calc_pc1(path, video_frame)

	# Get the concept.txt file
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
	print_file(inp, def_path+'inp.txt')
	
	# For relative frequency
	kgram = []
	for item in inp:
		if len(item)==3:
			kgram = kgram + item[2]
	#Remove the word inflections
	kgram = morphology(kgram)
	# Throw away the common kgrams
	kgram = exclude(kgram)
	#Sort and count
	kgram = sort_count(kgram)
	# You may try merging the smaller ones into bigger ones here to get better results	
	kgram = merge_same(kgram)
	# Ignore the kgrams having frequency 1
	i = len(kgram)-1
	while i>=0:
		if kgram[i][1]==1:
			kgram.pop(i)
		i = i-1
	print_func(kgram, def_path+'kgram.txt')	
	rf = []
	for item in kgram:
		for it in kgram_main:
			if item[0]==it[0] and it[1]!=0:
				temp = float(item[1])/float(it[1])
				rf.append([item[0],temp])
	
	rf.sort(key=mysort, reverse=True)
	print_func(rf, def_path+'rf.txt')

	
	# Joint probability of the concept and the label happening together
	jp = []
	for item in label:
		temp = 0.0
		for it in inp:
			if len(it)==3:
				if item in it[2]:
					temp = temp + it[1] - it[0]
		jp.append([item, temp/total_frame])
	
	
	#Conditional probability
	cp = []
	for item in jp:
		temp = item[1]/pc
		cp.append([item[0],temp])
	
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

	cp.sort(key=mysort, reverse=True)
	print_func(cp, def_path+'cp.txt')

	mi.sort(key=mysort, reverse=True)
	print_func(mi, def_path+'mi.txt')


if __name__=='__main__':
	main()
