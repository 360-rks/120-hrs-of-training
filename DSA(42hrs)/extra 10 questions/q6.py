"""
Question 6
For a given list of numbers find the its factors and add the factors then if the sum of all factor 
is present in original list, sort it and print it
Ex:
Input: 0,1,6
Factors: 0 = 0, sum =0
1 = 1, sum =1
6 =1,2,3 = sum =6
Output: 1,6
If the sum is not present in the list then return -1.
"""

l=[0,1,6,9]
fl=[]
for i in l:
    if i==0:
        fl.append([0])
    else:
        temp=[]
        for j in range(1,6):
            if i%j==0:
                temp.append(j)
        fl.append(temp)
fl_sum=[]
for i in fl:
    fl_sum.append(sum(i))
 
for i in fl_sum:
    if i in l:
        print(i,end=" ")
    else:
        print(-1,end=" ")
