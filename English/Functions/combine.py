#It will calculate the relative measure.
import sys

#Importing my personalised modules
sys.path.append('./Functions/')
from file_modify import *
from print_func import *
from sort_and_count import *

def my_sort(x):
	return x[-1]


def combine(target_path, c1_path, c2_path):
	jp1 = open(c1_path+'jp.txt').readlines()
	jp1 = map(file_modify_freq, jp1)
	jp2 = open(c2_path+'jp.txt').readlines()
	jp2 = map(file_modify_freq, jp2)
	ans = []
	
	for item in jp2:
		for it in jp1:
			if item[0]==it[0] and item[1]!=0:
				temp = it[1]/item[1]
				ans.append([item[0],temp])
	
	ans.sort(key=my_sort, reverse=True)
	print_func(ans, target_path+'jp.txt')
	del(ans)
	
	cp1 = open(c1_path+'cp.txt').readlines()
	cp1 = map(file_modify_freq, cp1)
	cp2 = open(c2_path+'cp.txt').readlines()
	cp2 = map(file_modify_freq, cp2)
	ans = []
	
	for item in cp2:
		for it in cp1:
			if item[0]==it[0] and item[1]!=0:
				temp = it[1]/item[1]
				ans.append([item[0],temp])
	
	ans.sort(key=my_sort, reverse=True)
	print_func(ans, target_path+'cp.txt')
	del(ans)

	mi1 = open(c1_path+'mi.txt').readlines()
	mi1 = map(file_modify_freq, mi1)
	mi2 = open(c2_path+'mi.txt').readlines()
	mi2 = map(file_modify_freq, mi2)
	ans = []
	
	for item in mi2:
		for it in mi1:
			if item[0]==it[0] and item[1]>0 and it[1]>0:
				temp = it[1]/item[1]
				ans.append([item[0],temp])
	
	ans.sort(key=my_sort, reverse=True)
	print_func(ans, target_path+'mi.txt')
	del(ans)
	
	rf1 = open(c1_path+'rf.txt').readlines()
	rf1 = map(file_modify_freq, rf1)
	rf2 = open(c2_path+'rf.txt').readlines()
	rf2 = map(file_modify_freq, rf2)
	ans = []
	
	for item in rf2:
		for it in rf1:
			if item[0]==it[0] and item[1]!=0 and ~(item[0]==1 and item[1]==1):
				temp = it[1]/item[1]
				ans.append([item[0],temp])
	
	ans.sort(key=my_sort, reverse=True)
	print_func(ans, target_path+'rf.txt')
	del(ans)
