class Queue:
    def __init__(self, max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
            
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
        
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
    
'''queue1=Queue(4)
print("Is it full",queue1.is_full())
print("Is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("element deleted",queue1.dequeue())
queue1.display()'''

print("----------------------------------------------")

queue2=Queue(3)
queue2.enqueue(11)
queue2.enqueue(22)
queue2.enqueue(33)
queue2.dequeue()
queue2.dequeue()
queue2.display()
queue2.enqueue(44)