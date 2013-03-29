#It will remove some common inflected words and will give them their root form

def morphology(x):
	i = 0
	while i<len(x):
		if x[i]=='triangles':
			x[i]='triangle'
		elif x[i]=='bigger':	
			x[i]='big'
		elif x[i]=='smaller':	
			x[i]='small'
		i = i+1
	return x
	
	
def morphology2(x):
	i = 0
	while i<len(x):
		if x[i]=='triangles':
			x[i]='triangle'
		elif x[i]=='big':	
			x[i]='bigger'
		elif x[i]=='small':	
			x[i]='smaller'
		i = i+1
	return x
