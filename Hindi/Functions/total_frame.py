#This function will return the total frames in the narrative corpus

def calc_tf(inp, error_check):
	# error_check = 1 indicates that the error check is on
	
	total_frame = 0							#All the frames in the narrative corpus
	tmp = 0									#Just for error detection
	for item in inp:
		if item[1]<=item[0] or (item[0]!=1 and item[0]!=tmp+1) and error_check==1:
			print "Error in file formatting at -"
			print str(item[0])+'\t\t'+str(item[1])
			quit()
		total_frame += item[1] - item[0] + 1
		tmp = item[1]
	return total_frame
