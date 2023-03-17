class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length

dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length",dam1.get_length())
