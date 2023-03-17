num1,num2,num3 = input().split(',')
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if(num1==7):
    print(num2*num3)
elif(num2==7):
    print(num3)
elif(num3==7):
    print(-1)
else:
    print(num1*num2*num3)