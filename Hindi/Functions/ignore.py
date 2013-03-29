# Deletes the strings having the mentioned frequency

def ignore_freq(db_word, freq):
	i = len(db_word)-1
	while i>=0:
		if db_word[i][1]==freq:
			db_word.pop(i)
		i = i-1
	return db_word
