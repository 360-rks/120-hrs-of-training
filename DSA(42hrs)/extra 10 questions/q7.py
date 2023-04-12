"""
question 7
Maximum subarray
An array is given suppose a =[3,5,8,2,19,12,7,11] One have to find the largest subarray that the 
element satisfy the following condition
x[i]=x[i-1]+x[i-2] If more than one substring if found then largets one has to print the array 
which starts with the minimum elements and if they are also same then the array with minimum 
second element and so on.
Here the subarrays= [3, 5, 8], [3, 8, 11, 19], [2, 3, 5, 8], [2, 5, 7, 12, 19], [5, 7, 12, 19], [8, 11, 19], [7, 12, 19] 
Expected output is [2, 5, 7, 12, 19]
"""
arr =[3,5,8,2,19,12,7,11]
temp=[]
for i in arr:
    for j in arr:
        if i!=j:
            for k in arr:
                if i!=j!=k:
                    if i+j==k:
                        temp.append([i,j,k])

subarr=[]
for i in temp:
    i.sort()
    if i not in subarr:
        subarr.append(i)

for x in range(len(arr)-3):
    for i in subarr:
        for j in arr:
            if j not in i:
                if i[-2]+i[-1]==j:
                    i.append(j)


maxl=0
for i in subarr:
    if len(i)>maxl:
        maxl=len(i)
result=list(filter(lambda x:len(x)==maxl,subarr))
if len(result)==1:
    print(result[0])
else:
    print(min(result))

