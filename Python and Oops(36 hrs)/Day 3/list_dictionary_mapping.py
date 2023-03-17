mylist = list(map(int,input().split()))
list_b = list(map(int,input().split()))

print(mylist)
print(list_b)

result={}
for i in list_b:
    result[i]= mylist.index(i)
print(result)

print({i:mylist.index(i) for i in list_b})
    

             


