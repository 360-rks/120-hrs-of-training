#1 Positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4,end=" ")
    print()
function1(10,20,30,40)
function1(100,'200',300,400)

#2 Keyword arguments
def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4,end=" ")
    print()
function2(num4=10,num1=20,num2=30,num3=40)
function2(100,'200',300,400)#data is sent right to left


#3 Default Arguments
def function3(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)#college is explicitly set first
function3("Ayush",147)
function3("Sumit",3,"CST")
