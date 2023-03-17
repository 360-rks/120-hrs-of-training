class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
    
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())