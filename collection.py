import sys
import MySQLdb

stat = sys.argv[1]
# This is the line to connect to our MYSQL
db=MySQLdb.connect(host="localhost",user="root",passwd="MiLpOk01!MiLeS01!",db="sales")

#you must create a Cursor object. It will let
# you execute all the queries you need
cur=db.cursor()

cur.execute("select * from transactions as t join info i on t.name=i.name where status='"+stat+"';")

for row in cur.fetchall():
	print "Client: " + row[2] + "   Phone #: " + row[8] + "   Address: " + row[9]
	
db.close