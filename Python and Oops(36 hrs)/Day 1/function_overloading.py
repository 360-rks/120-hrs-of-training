#function overloading

def function4(*var):
    for i in var:
        print(i,end=' ')
        
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)
print()


def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)

print(add(10,30))
print(add(10,20,30))
print(add(10,20,30,40))