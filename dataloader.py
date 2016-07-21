import sys
import MySQLdb

# This is the line to connect to our MYSQL
db=MySQLdb.connect(host="localhost",user="root",passwd="MiLpOk01!MiLeS01!",db="sales")

#you must create a Cursor object. It will let
# you execute all the queries you need
cur=db.cursor()
ln=0
f=open('dataprimer.csv','r')
for line in f:
	#if line.startswith('date'):
	if ln < 3:
		pass
	else:
		line=line.strip('\n').strip('\r')
		entry=line.split(',')
		print entry
		
		query="INSERT INTO transactions(date,name,cost,paid,balance,status) VALUES ('"+entry[0]+"','"+entry[1]+"','"+entry[2]+"','"+entry[3]+"','"+entry[4]+"','"+entry[5]+"')"
		
		print query

		cur.execute(query)
		db.commit()
	ln+=1