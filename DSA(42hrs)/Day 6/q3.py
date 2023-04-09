'''The owner of a BakeHouse wants to keep track of the tables 
that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class. 
Represent occupied_table_list using an appropriate data 
structure.


Note: Table numbers should be maintained in ascending order in the occupied_table_list.


Tables should be allocated and de-allocated as mentioned in the example below:

Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be allocated table 2 as it is the first free table.


Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method.
-------------------------------------------------------
10.Write a python program to reverse a linked list containing 
integer data.
Use the LinkedList class and methods in it to implement the
 above program.'''
class node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class slinkedList:
    def __init__(self):
        self.headNode=None
    
    def insertInSortedWay(self,data):
        if self.headNode==None:
            self.headNode=node(data)
            return
        elif self.headNode.data>data:
            temp=self.headNode
            self.headNode=node(data)
            self.headNode.nextNode=temp
            return
        itr=self.headNode
        while itr.nextNode!=None and itr.nextNode.data<data:
            itr=itr.nextNode
        temp=itr.nextNode
        itr.nextNode=node(data)
        itr.nextNode.nextNode=temp
    
    def delete(self,data):
        if self.headNode==None:
            print("list is empty")
            return
        elif self.headNode.data==data:
            self.headNode=self.headNode.nextNode
            return
        itr=self.headNode
        while itr.nextNode!=None and itr.nextNode.data!=data:
            itr=itr.nextNode
        itr.nextNode=itr.nextNode.nextNode
    
    def findAvailableTable(self):
        l=[1,2,3,4,5,6,7,8,9,10]
        itr=self.headNode
        otl=[]
        while itr !=None:
            otl.append(itr.data)
            itr=itr.nextNode

        for i in range(1,11):
            if i not in otl:
                return i
            if i==10:
                print("all tables occupied")
                return False
        
    

    
    def printList(self):
        itr=self.headNode
        while itr !=None:
            print(itr.data,end=" ")
            itr=itr.nextNode
        print()

        
class bakeHouse:
    def __init__(self,occupied_table_list):
        self.occupied_table_list=occupied_table_list
    
    def get_occupied_table_list(self):
        self.occupied_table_list.printList()
        return self.occupied_table_list
    def allocate_table(self):
        temp=self.occupied_table_list.findAvailableTable()
        if temp!=False:
            self.occupied_table_list.insertInSortedWay(temp)
    
    def deallocate_table(self,table_number):
        self.occupied_table_list.delete(table_number)

l1=slinkedList()
l1.insertInSortedWay(1)
l1.insertInSortedWay(2)
l1.insertInSortedWay(3)
l1.insertInSortedWay(4)
l1.printList()
bh1=bakeHouse(l1)
bh1.allocate_table()
bh1.get_occupied_table_list()
bh1.deallocate_table(2)
bh1.get_occupied_table_list()
bh1.allocate_table()
bh1.get_occupied_table_list()

bh1.allocate_table()
l1.printList()
bh1.allocate_table()
bh1.allocate_table()
bh1.allocate_table()
bh1.allocate_table()
bh1.allocate_table()
bh1.allocate_table()
bh1.allocate_table()
l1.printList()