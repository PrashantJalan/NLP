# This function merges the smaller k-grams into the bigger ones.
# This is_subgram return a Bollean value stating if x is subgram of y
# The merge_same function merges the smaller into bigger when the value for both is same.
# The merge function does this when the value for the smaller is smaller than the bigger.
from syllable import *
from kgrams import *

def is_subgram(x,y):
	#Checks if x is a subgram of y
	a = get_syll(x,1)
	b = get_syll(y,1)
	z = b+kgrams(b, ['2','3','4','5','6','7','8','9','10'])

	if len(a)>=len(b):
		return False
	else:
		i = 0
		if x in z:
			return True
		else:
			return False
	
def merge(li):
	#Assumes that the list is sorted
	for item in li:
		if len(item)!=2:
			print "The passed in list doesn't contain two attributes."
			quit()

	syll = []
	kgram = []
	length = []
	for item in li:
		tmp = get_syll(item[0],1)
		syll.append(tmp)
		length.append(len(tmp))
		tmp2 = tmp+kgrams(tmp, ['2','3','4','5','6','7','8','9','10'])
		kgram.append(tmp2)

	i = len(li)-1
	while i>=0:
		j = len(li)-1
		while j>=0:
			if li[i][1]==li[j][1] and length[i]<length[j]:
				if li[i][0] in kgram[j]:
					li.pop(i)
					syll.pop(i)
					length.pop(i)
					kgram.pop(i)
					break
			j = j-1
		i = i-1
	return li
		
def merge_same(li):
	#Assumes that the list is sorted
	for item in li:
		if len(item)!=2:
			print "The passed in list doesn't contain two attributes."
			quit()

	syll = []
	kgram = []
	length = []
	for item in li:
		tmp = get_syll(item[0],1)
		syll.append(tmp)
		length.append(len(tmp))
		tmp2 = tmp+kgrams(tmp, ['2','3','4','5','6','7','8','9','10'])
		kgram.append(tmp2)

	i = len(li)-1
	while i>=0:
		j = len(li)-1
		while j>=0:
			if li[i][1]<=li[j][1] and length[i]<length[j]:
				if li[i][0] in kgram[j]:
					li.pop(i)
					syll.pop(i)
					length.pop(i)
					kgram.pop(i)
					break
			j = j-1
		i = i-1
	return li
