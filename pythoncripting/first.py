f=None
with open ("scores.txt","r") as f:
	score = 0
	for line in f:
		score += int(line)
		print (f.closed)
#vichar kara
