array = ["ibad","john","stephen"]
for i in range(len(array)):
	print array[i]
	
dic = {"name":"mike","pass":"bigboy"}
for i in dic:
	print dic[i]

arr = []
arr.append(7)
arr.append(8)
print arr[1]	

class Link(object):
	def __init__(self,bookname,sold):
		self.name = bookname
		self.sold = sold;
		self.next = None;
		
	def display(self):
		print self.name + ": " + str(self.sold) + " million sold"

class LinkList(object):
	def __init__(self):
		self.firstlink = None;
		
	def isEmpty(self):
		return (self.firstlink==None)
	
	def insertFirst(self,bookname,sold):
		newLink = Link(bookname,sold)
		newLink.next = self.firstlink
		self.firstlink = newLink
		
	def display(self):
		theLink = self.firstlink
		while theLink is not None:
			theLink.display();
			theLink = theLink.next
			
	def removeFirst(self):
		linkReference = self.firstlink
		if not self.isEmpty():
			self.firstlink = self.firstlink.next
		else:
			print "The list is empty!"
		return linkReference
		
	def find(self,bookName):
		linkReference = self.firstlink
		if linkReference is None:
			print "The list is empty"
		else:
			while linkReference.name != bookName:
				if linkReference.next is None:
					print "No such book exists"
					return
				else:
					linkReference = linkReference.next
			linkReference.display();
			
	def remove(self,bookName):
		current = self.firstlink
		previous = self.firstlink
		if not self.isEmpty():
			while current.name != bookName:
				if(current.next is None):
					print bookName + " is not in the list"
					return
				else:
					previous = current;
					current = current.next
			if previous == current:
				self.firstlink = self.firstlink.next
			else:
				previous.next = current.next
			print current.name + " was removed"

LL = LinkList();
LL.insertFirst("Harry Potter",107)
LL.insertFirst("The Bog Short",215)
LL.insertFirst("Big bang",314)
LL.insertFirst("Swoley bible",515)
#LL.find("Harry Potter")
#LL.removeFirst();
LL.remove("Swoley bible")
LL.display()
		
user = input("Enter tree height:")
user = int(user)

space = user - 1
end = space 
hash = 1

while(user > 0):
	print((" " * space) + ("#" * hash))
	space -=1
	hash+=2
	user-=1
	
print((" " * end) + "#")


	
	
	
	
	