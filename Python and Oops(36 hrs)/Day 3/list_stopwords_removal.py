sentences=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on teusday",
           "with over three lakhs diya or earthen lamps",
           "lit up simultaneously on the bank of river sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was"]

result=[]
for i in sentences:
    temp = list(i.split())
    for j in temp:
        result.append(j)
print(result)

for i in stopwords:
    for j in result:
        if(i==j):
            result.remove(i)
        
print(result)

sentences=["a new world record was set","in the holy city of ayodhya","on the eve of divali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was"]
result= []
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
    
print(result)

sentences=["a new world record was set","in the holy city of ayodhya","on the eve of divali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was"]
l=[]
for i in sentences:
    temp=list(i.split())
    for j in temp:
        for k in stopwords:
            if j==k:
                temp.remove(k)
    s=" ".join(temp)
    l.append(s)
print(l)

print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])