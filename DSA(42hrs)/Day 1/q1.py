'''Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.

Note: A number is said to be evenly divisible if it is divisble by all the numbers in the given range without any reaminder.
Consider the range to be from 1 to 10 (both inclusive)
Assume that there will always be few elements in the input queue, which are evenly divisible by the  numbers in the mentioned
range.

Example:
Input Queue: 13983,10080,7113,2520,2500(front -rear)
Output Queue: 10080,2520(front-rear)'''

class queue:
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__front=0
        s.__rare=-1
    def isfull(s):
        if(s.__rare==s.__max_size-1):
            return True
        return False
    def isempty(s):
        if(s.__front>s.__rare):
            return True
        return False
    def enqueue(s,val):
        if(s.isfull()):
            print("Queue is full")
        else:
            s.__rare+=1
            s.__element[s.__rare]=val
            # print("inserted {} in the Queue".format(s.__element[s.__rare]))
    def dqueue(s):
        if(s.isempty()):
            print("Queue is empty")
        else:
            x=s.__element[s.__front]
            s.__element[s.__front]=None
            s.__front+=1
            # print("Deleted {} in the Queue".format(x))
            return x
    def get_max_size(s):
        return s.__max_size
    def display(s):
        # print("The Queue elements are: ",end="")
        print(','.join([str(s.__element[i]) for i in range(s.__front,s.__rare+1)]))
    def front(s):
        return s.__element[s.__front]
    
def evenly_number(q):
    size=q.get_max_size()
    q1=queue(size)
    while(size>0):
        x=q.dqueue()
        f=1
        for i in range(1,11):
            if(x%i!=0):
                f=0
                break
        if(f==1):
            q1.enqueue(x)
        size-=1
    return q1

a=int(input())
q1=queue(a)
l=[int(i) for i in input().split(",")]
for i in l:
    q1.enqueue(i)
q2=evenly_number(q1)
q2.display()