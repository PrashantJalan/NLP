#This code gets the label probability

def calc_pl(x):
	total = 0.0
	for item in x:
		total = total + item[1]
	i = 0
	y = []
	while i<len(x):
		temp = float(x[i][1])/total
		y.append([x[i][0],temp])
		i = i+1
	return y
