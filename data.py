import sys

f = open("dataprimer.csv","r")
ln = 0
total=0
for line in f:
	if ln > 0:
		line = line.strip("\n")
		entry = line.split(",")
		total += int(entry[4])	
		print total
	ln +=1
print total

f.close