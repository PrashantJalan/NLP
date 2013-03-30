# The functions below help check the involvement of x into y
# x and y denote frame nos. If y is a part of x then result is 1 (100%)

def involved(x,y):
	if x[1]<y[0] or x[0]>y[1]:
		return 0
	elif x[1]>=y[1] and x[0]<=y[0]:
		return 1
	elif x[0]>y[0] and x[1]<y[1]:
		return (float)(x[1]-x[0])/(float)(y[1]-y[0])
	elif x[0]>y[0] and x[1]>=y[1]:
		return (float)(y[1]-x[0])/(float)(y[1]-y[0])
	elif x[0]<=y[0] and x[1]<y[1]:
		return (float)(x[1]-y[0])/(float)(y[1]-y[0])
