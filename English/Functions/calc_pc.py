# This functions calculates the probability of the happening of a particular concept
# calc_pc1 calculates the P(c) based on the movement record
# calc_pc2 calculates the P(c) based on the extracted text

from file_modify import *
from total_frame import *

def calc_pc1 (mr_path, frames):
	# mr_path is the path of the movement record file
	# frames is the total no. of frames in the video
	
	mr = open(mr_path).readlines()
	mr = map(file_modify,mr)
	mr_frame = calc_tf(mr, 0)
	pc = float(mr_frame)/float(frames)
	return pc

def calc_pc1 (c_path, frames):
	# c_path is the path of the concept file
	# frames is the total no. of frames in the narrative corpus
	
	c = open(c_path).readlines()
	c = map(file_modify,c)
	c_frame = calc_tf(c, 0)
	pc = float(c_frame)/float(frames)
	return pc
