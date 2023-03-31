class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next = self.head
            self.head.previous= new_node
            self.head=new_node
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=" ")
            temp=temp.next

x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtBeginning(5)
x.printLinkedList()
x.insertAtBeginning(15)
x.insertAtBeginning(25)
x.insertAtBeginning(35)
x.printLinkedList()
print("no of nodes",x.length())
