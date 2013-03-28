#It will remove some common inflected words and will give them their root form

def morphology(x):
	i = 0
	while i<len(x):
		if x[i]==u'\u0928\u0940\u0932\u0947':		#neele to neela
			x[i]=u'\u0928\u0940\u0932\u093e'
		elif x[i]==u'\u091b\u094b\u091f\u0947':		#chote to chota
			x[i]=u'\u091b\u094b\u091f\u093e'
		elif x[i]==u'\u092c\u0921\u093c\u0947':		#bade to bada
			x[i]=u'\u092c\u0921\u093c\u093e'
		i = i+1
	return x
