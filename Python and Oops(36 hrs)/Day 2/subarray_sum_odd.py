starting_index = int(input())
ending_index = int(input())
l = list(map(int,input().split()))

list2=[]
for i in range(len(l)+1):
    for j in range(i):
        list2.append(l[j:i])
        
print(list2)
count = 0
for i in list2:
    if(sum(i)%2!=0):
        count+=1
        
print(count)



