"""
orignal list=
12
95
140
110
40

n=100

new list=
12
95
100
110
40

put n in place of max value of the orignal list
"""
class node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class sLinkedList:
    def __init__(self):
        self.headNode=None
    
    def insertAtEnd(self,data):
        if self.headNode ==None:
            self.headNode=node(int(data))
            return
        itr=self.headNode
        while itr.nextNode !=None:
            itr=itr.nextNode
        itr.nextNode=node(int(data))
    
    def printList(self):
        itr=self.headNode
        while itr !=None:
            print(itr.data,end="->")
            itr=itr.nextNode
        print()
    
    def maxValue(self):
        temp=0
        itr=self.headNode
        while itr!=None:
            if temp<itr.data:
                temp=itr.data
            itr=itr.nextNode
        return temp
    
def maxKiller(llist,n):
    maxx=llist.maxValue()
    print(maxx)
    itr=llist1.headNode
    while itr.data!=maxx:
        itr=itr.nextNode
    itr.data=n
    



llist1=sLinkedList()
list(map(llist1.insertAtEnd,input().split()))
llist1.printList()
n=int(input())
maxKiller(llist1,n)
llist1.printList()