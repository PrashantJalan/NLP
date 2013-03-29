# corpus.txt contains the most common words in English. exclude function
# will exclude the most common words from the narrative word database
# Source: http://www.world-english.org/english500.htm

def exclude(x):
	corpus = open("Files/corpus.txt").readlines()
	
	i = 0
	while i<len(corpus):
		corpus[i] = corpus[i].strip()
		i = i+1

	i = 0
	while i<len(x):
		if x[i] in corpus:
			x.pop(i)
		else:
			i = i+1
	
	return x
