array = list(map(int,input().split(",")))
number1 = sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l = array[array.index(5):array.index(8)+1]
number2=""
for i in l:
    number2+=str(i)
print(int(number2)+number1)

