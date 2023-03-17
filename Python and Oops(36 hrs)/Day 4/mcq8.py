class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    
    def purchase(self):
        self.display()
        print("Calculating price")

Mobile().purchase()
Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2
print(m1)
print(m2)


