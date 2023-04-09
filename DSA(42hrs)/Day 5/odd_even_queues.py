class Queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.front = 0
        self.rare = -1
        self.element = [None]*max_size

    def is_full(self):
        if self.front == self.max_size-1:
            return True
        return False

    def is_empty(self):
        if self.rare < self.front:
            return True
        return False

    def enque(self,data):
        if (self.is_full()):
            print("Queus is Full")
        else:
            self.rare+=1
            self.element[self.rare] = data

    def e_o(self):
        for i in range(self.front,self.rare):
            print(self.element[i],end='')

    def display(self):
        odd =0
        even =0
        l=[]
        for i in range (self.front,self.rare+1):
            l.append(self.element[i])
            if self.element[i] % 2 ==0:
               even+=1
            else:
                odd+=1
        qe= Queue(even)
        qo =Queue(odd)

        for i in l:
            if i%2==0:
                qe.enque(i)
            else:
                qo.enque(i)

        print("odd")
        qo.e_o()
        print()
        print("even")
        qe.e_o()



q1 = Queue(7)
q1.enque(2)
q1.enque(7)
q1.enque(9)
q1.enque(4)
q1.enque(6)
q1.enque(5)
q1.enque(10)
q1.display()