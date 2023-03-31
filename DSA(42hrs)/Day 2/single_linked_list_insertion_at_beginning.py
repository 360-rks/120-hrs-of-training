class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
    
   def AtBegining(self,newdata):#"sun"
       NewNode = Node(newdata) 
       # Update the new nodes next val to existing node
       NewNode.nextval=self.headval 
       self.headval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first node to second node
list.headval.nextval = e2

#Link second Node to third node
e2.nextval = e3
#list.headval.nextval.nextval = e3
list.AtBegining("Sun")

list.listprint()