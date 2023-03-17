n1=int(input("Enter the value of n1:"))
n2= int(input("Enter the value of n2:"))
array=[i for i in range(n1,n2+1)]
print(array)
result=[]
'''for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)'''
l1=[array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
print(l1)
c=0
for i in l1:
    if(sum(i)%2!=0):
        c+=1
print(c)