import sys

f = open("dataprimer.csv","r")

total=0
cost=0
paid=0
for line in f:
	line = line.strip("\n")
	entry = line.split(",")
	try:
		total += int(entry[4])
		cost += int(entry[2])
		paid += int(entry[3])
	except:
		pass

print "Balance: " + str(total)
print "Cost: " + str(cost)
print "Paid: " + str(paid)

status = sys.argv[1]
total_stat = 0
total=0
cost=0
paid=0
f.seek(0)
for line in f:
	line = line.strip("\n")
	entry = line.split(",")
	try:
		if entry[5] == status:
			total_stat+=1
			total += int(entry[4])
			cost += int(entry[2])
			paid += int(entry[3])
			print "Client with " + status + " balance: " + entry[1]
	except:
		pass
print "There are a total of " + str(total_stat) + " clients with " + status + " status."
print "Balance for all " + status + " cases = " + str(total)
print "Cost for all " + status + " cases = " + str(cost)
print "Paid for all " + status + " cases = " + str(paid)
f.close