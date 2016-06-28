import sys

personName = sys.argv[1]

print "Hello " + personName
timetable=int(sys.argv[2])
for i in range(1,11):
	print str(timetable) + " x " + str(i) + " = " + str(timetable*i)
	

num = 1
while num<11:	
	print timetable*num
	num+=1

