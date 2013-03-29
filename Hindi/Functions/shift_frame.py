#It shifts the frame to accomodate the verbal delay for the speakers

def shift_frame(mr, delay):
	i = 0
	while i<len(mr):
		mr[i][0] = mr[i][0] + delay
		mr[i][1] = mr[i][1] + delay
		i = i+1
	return mr
