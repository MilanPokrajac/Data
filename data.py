import sys

f = open("dataprimer.csv","r")

total=0
for line in f:
	try:
		line = line.strip("\n")
		entry = line.split(",")
		total += int(entry[4])	
	except:
		pass

print total

f.close
