#List Comprehension

#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)

#list comprehension version
print([i for i in range(11)])
#for loop version-->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])




