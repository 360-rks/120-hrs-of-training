'''Write a python function which accepts two linked lists containing integer data and an integer ,n merges the two linked
lists, such that list2 is merged with list1 after n number of nodes.
Assume that value of n will always be less than or equal to the number of nodes in list 1

Sample Input                       Expected Output
list1                              1->2->4->3->5
list2                              9->8->11
n - 2                              1->2->9->8->11->4->3->5 '''

def listMerger(ll1,ll2,n):
    counter=1
    itr=ll1.headNode
    while(counter<n):
        counter+=1
        itr=itr.nextNode
    temp=itr.nextNode
    itr.nextNode=ll2.headNode
    itr2=ll2.headNode
    while itr2.nextNode!=None:
        itr2=itr2.nextNode
    itr2.nextNode=temp
    return ll1
    

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



llist1=sLinkedList()
llist2=sLinkedList()
list(map(llist1.insertAtEnd,input().split("->")))
list(map(llist2.insertAtEnd,input().split("->")))
print("llist1=")
llist1.printList()
print("llist2=")
llist2.printList()
print("enter value of n: ",end="")
n=int(input())
print("llist1 after merge=")
llist1=listMerger(llist1,llist2,n)
llist1.printList()