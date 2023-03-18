class Car:
    
    def __init__(self):
        self.__att1 = None
        self.__att2 = None
        self.__att3 = None
        self.__att4 = None
        
    def set_attributes(self,id_of_car,type_of_car,cost):
        self.__att1=id_of_car
        self.__att2=type_of_car
        self.__att3=cost
        
    def premium_calc(self):
        if self.__att2=="two wheelers":
            self.__att4 = self.__att3*0.02
        elif self.__att2=="four wheelers":
            self.__att4 = self.__att3*0.06
        else:
            print("Invalid")
            

    def get_attributes(self):
        self.premium_calc()
        return self.__att4

    def get_id(self):
        return self.__att1 
    
    def get_type(self):
        return self.__att2

c1 = Car()
c1.set_attributes(101, "Two Wheelers".lower(), 500000)
print(c1.get_id(),c1.get_type(),c1.get_attributes())
c2=Car()
c2.set_attributes(102, "Four Wheelers".lower(), 500000)
print(c2.get_id(),c2.get_type(),c2.get_attributes())

    
    

        