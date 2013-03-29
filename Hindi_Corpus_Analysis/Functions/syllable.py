#We couldn't use our syllable function because that is quite slow

def get_syll(x):
	#States - store, ignore, initial, consonant, vowel, halant
	state = 'initial'
	li = x
	syll = []

	i = 0
	while True:
		if state=='store':
			syll.append(tmp)
			del(tmp)
			state = 'initial'
		elif i>=len(li):
			if 'tmp' in locals():
				state = 'store'
			else:
				break
		elif state=='initial':
			tmp = li[i]
			i = i+1
			if tmp==u'\u0950':
				state = 'store'
			elif (tmp>=u'\u0915' and tmp<=u'\u0939') or (tmp>=u'\u0958' and tmp<=u'\u095F'):
				state = 'consonant'
			elif tmp>=u'\u0904' and tmp<=u'\u0914':
				state = 'vowel'
			else:
				state = 'ignore'
		elif state=='ignore':
			del(tmp)
			state = 'initial'
		elif state=='consonant':
			tmp2 = li[i]
			if tmp2>=u'\u093E' and tmp2<=u'\u094C':
				tmp = tmp+tmp2
				i = i+1
			elif (tmp2>=u'\u0900' and tmp2<=u'\u0903') or tmp2==u'\u093C':
				tmp = tmp+tmp2
				i = i+1
			elif tmp2==u'\u094D':
				tmp = tmp+tmp2
				i = i+1
				state = 'halant'
			else:
				state = 'store'
		elif state=='vowel':
			tmp2 = li[i]
			if (tmp2>=u'\u0900' and tmp2<=u'\u0903') or tmp2==u'\u093C':
				tmp = tmp+tmp2
				i = i+1
				state = 'store'
			else:
				state = 'store'
		elif state=='halant':
			tmp2 = li[i]
			if (tmp2>=u'\u0915' and tmp2<=u'\u0939') or (tmp2>=u'\u0958' and tmp2<=u'\u095F'):
				tmp = tmp+tmp2
				i = i+1
				state = 'consonant'
			else:
				state = 'store'
		
	return syll
