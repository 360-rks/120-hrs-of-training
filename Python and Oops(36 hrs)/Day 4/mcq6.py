class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
        
s1=Shoe(1000,"Canvas")
print(s1)
print("the unique id of thr object",id(s1))


