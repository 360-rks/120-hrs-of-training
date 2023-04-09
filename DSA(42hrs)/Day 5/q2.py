"""there is a queue with data of different persons, data has name,age, gender.
user inputs male or female
if input is male display data of male persons, and vice versa."""

class queue:
    def __init__(self,size):
        self.maxsize=size
        self.l=[]
    def isFull(self):
        if len(self.l)==self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.l)==0:
            return True
        else:
            return False    

    def lenQueue(self):
        return len(self.l)    

    def enqueue(self,data):
        if self.isFull():
            print("queue is full")
        else:
            self.l.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            x=self.l.pop(0)
            return x
    
    def printQueue(self):
        for i in self.l:
            print(i,end=" ")
    
def getPerson(q,gender):
    for i in range(q1.lenQueue()):
        temp=q1.dequeue()
        if temp[2]==gender:
            print(temp)
        q1.enqueue(temp)   

p1=["aaa",11,"male"]
p2=["bbb",22,"female"]
p3=["ccc",33,"female"]
p4=["ddd",44,"male"]
p5=["eee",55,"male"]
p6=["fff",66,"female"]
q1=queue(6)
q1.enqueue(p1)
q1.enqueue(p2)
q1.enqueue(p3)
q1.enqueue(p4)
q1.enqueue(p5)
q1.enqueue(p6)
q1.printQueue()
print("===============================================================================")
getPerson(q1,"female")
print("===============================================================================")
getPerson(q1,"male")
print("===============================================================================")
q1.printQueue()