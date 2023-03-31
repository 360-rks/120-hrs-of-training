'''Given two queues, one integer queue and another character queue, write a python program to merge them to form a single
queue.Follow the below rules for merging:
Merge elements at the same position starting with the integer queue. 
If one of the queues has more elements than the other, add all the additional elements at the end of the output queue.
Note: max_size of the merged queue should be the sum of the size of both the queues.

For example
Input-- queue1:3,6,8  queue2: b,y,u,t,r,o
Output -- 3,b,6,y,8,u,t,r,o
'''
class queues:
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
        print()
    def front(s):
        return s.__element[s.__front]

def merge(q1,q2):
    s1=q1.get_max_size()
    s2=q2.get_max_size()
    q=queues(s1+s2)
    if(s1>=s2):
        for i in range(s2):
            q.enqueue(q1.dqueue())
            q.enqueue(q2.dqueue())
        for i in range(s1-s2):
            q.enqueue(q1.dqueue())
    else:
        for i in range(s1):
            q.enqueue(q1.dqueue())
            q.enqueue(q2.dqueue())
        for i in range(s2-s1):
            q.enqueue(q2.dqueue())
    q.display()

n=int(input())
m=int(input())
q_int=queues(n)
q_char=queues(m)
l_int=[q_int.enqueue(int(i)) for i in input().split(',')]
l_char=[q_char.enqueue(i) for i in input().split(',')]
merge(q_int,q_char)