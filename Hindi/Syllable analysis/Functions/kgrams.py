#Given a list of syllable it will return the k-gram based on the type of k-gram required
#The type of k-gram can contain numerals from 2 to 10

def kgrams (syllable, type_of_kgram):
	
	ans = []

	if '2' in type_of_kgram:
		i=0
		while i<len(syllable)-1:
			temp = ''.join([syllable[i],syllable[i+1]])
			ans.append(temp)	
			i=i+1

	if '3' in type_of_kgram:
		i=0
		while i<len(syllable)-2:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2]])
			ans.append(temp)	
			i=i+1

	if '4' in type_of_kgram:
		i=0
		while i<len(syllable)-3:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2],syllable[i+3]])
			ans.append(temp)	
			i=i+1

	if '5' in type_of_kgram:
		i=0
		while i<len(syllable)-4:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2],syllable[i+3],syllable[i+4]])
			ans.append(temp)	
			i=i+1
	
	if '6' in type_of_kgram:
		i=0
		while i<len(syllable)-5:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2],syllable[i+3],syllable[i+4],syllable[i+5]])
			ans.append(temp)	
			i=i+1

	if '7' in type_of_kgram:
		i=0
		while i<len(syllable)-6:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2],syllable[i+3],syllable[i+4],syllable[i+5],syllable[i+6]])
			ans.append(temp)
			i=i+1

	if '8' in type_of_kgram:
		i=0
		while i<len(syllable)-7:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2],syllable[i+3],syllable[i+4],syllable[i+5],syllable[i+6],syllable[i+7]])
			ans.append(temp)
			i=i+1

	if '9' in type_of_kgram:
		i=0
		while i<len(syllable)-8:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2],syllable[i+3],syllable[i+4],syllable[i+5],syllable[i+6],syllable[i+7],syllable[i+8]])
			ans.append(temp)
			i=i+1

	if '10' in type_of_kgram:
		i=0
		while i<len(syllable)-9:
			temp = ''.join([syllable[i],syllable[i+1],syllable[i+2],syllable[i+3],syllable[i+4],syllable[i+5],syllable[i+6],syllable[i+7],syllable[i+8],syllable[i+9]])
			ans.append(temp)
			i=i+1

	return ans
