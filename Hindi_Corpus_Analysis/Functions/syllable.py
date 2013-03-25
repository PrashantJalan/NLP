# Given a string, it will return a list of syllables for the string
# Works for Hindi text
# NOTE: We do not account for every symbol that was/is used in Hindi. We have taken only the symbols we understand ourselves.

import codecs

def is_consonant(x):
	# Returns true is x is a consonant
	if x>=u'\u0915' and x<=u'\u0928':
		return True
	elif x>=u'\u092A' and x<=u'\u0930':
		return True
	elif x>=u'\u0932' and x<=u'\u0933':
		return True
	elif x>=u'\u092A' and x<=u'\u0930':
		return True
	elif x>=u'\u0935' and x<=u'\u0939':
		return True
	else:
		return False

def is_vowel(x):
	# Returns true if x is a vowel
	if x>=u'\u0904' and x<=u'\u0914':
		return True
	else:
		return False
	
def is_halant(x):
	# Returns true if x is a halant
	if x==u'\u094D':
		return True
	else:
		return False

def is_matra(x):
	# Returns true if x is a matra
	if x>=u'\u093E' and x<=u'\u094C':
		return True
	else:
		return False

def is_numeral(x):
	# Returns true if x is numeral
	if x>=u'\u0966' and x<=u'\u096F':
		return True
	else:
		return False

def is_om(x):
	# Returns true if x is a halant
	if x==u'\u0950':
		return True
	else:
		return False

def is_punctuation(x):
	# Returns true if x is a purna viram
	if x==u'\u0964' or x==u'\u0965':
		return True
	else:
		return False

def is_sign(x):
	# Returns true if x is a sign
	if x>=u'\u0900' and x<=u'\u0903':
		return True
	elif x==u'\u093C':
		return True
	else:
		return False


def get_syll(x, error_check):
	# error_check = 1 indicates that the error check is on
	if error_check==1:
		for item in x:
			if is_consonant(item)==False and is_matra(item)==False and is_halant(item)==False and is_vowel(item)==False and is_numeral(item)==False and is_om(item)==False and is_sign(item)==False:
				print "Found a symbol which doesn't belong to any recognised Hindi Unicode character"
				quit()
	
	#States - store, ignore, initial, consonant, vowel, halant
	state = 'initial'
	li = list(x)
	syll = []

	while True:
		if state=='store':
			syll.append(tmp)
			del(tmp)
			state = 'initial'
		elif len(li)==0:
			if 'tmp' in locals():
				state = 'store'
			else:
				break
		elif state=='initial':
			tmp = li.pop(0)
			if is_sign(tmp)==True or is_punctuation(tmp)==True or is_halant(tmp)==True or is_numeral(tmp)==True:
				state = 'ignore'
			elif is_om(tmp)==True:
				state = 'store'
			elif is_consonant(tmp)==True:
				state = 'consonant'
			elif is_vowel(tmp)==True:
				state = 'vowel'
			else:
				state = 'ignore'
		elif state=='ignore':
			del(tmp)
			state = 'initial'
		elif state=='consonant':
			tmp2 = li.pop(0)
			if is_matra(tmp2)==True:
				tmp = tmp+tmp2
			elif is_sign(tmp2)==True:
				tmp = tmp+tmp2
			elif is_halant(tmp2)==True:
				tmp = tmp+tmp2
				state = 'halant'
			else:
				li.insert(0,tmp2)
				state = 'store'
		elif state=='vowel':
			tmp2 = li.pop(0)
			if is_sign(tmp2)==True:
				tmp = tmp+tmp2
				state = 'store'
			else:
				li.insert(0,tmp2)
				state = 'store'
		elif state=='halant':
			tmp2 = li.pop(0)
			if is_consonant(tmp2)==True:
				tmp = tmp+tmp2
				state = 'consonant'
			else:
				li.insert(0,tmp2)
				state = 'store'
	return syll
