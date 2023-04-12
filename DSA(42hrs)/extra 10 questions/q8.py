"""
Question 8
 Special string reverse
special string reverse
Input Format: b@rd
output Format: d@rb
Explanation:
We should reverse the alphabets of the string by keeping the 
special characters in the same position.
"""
s="b@rd&ab#"
l=[]
d={}
for idx,ele in enumerate(s):
    if ele.isalpha()==False:
        d[idx]=ele
for i in s[::-1]:
    if i.isalpha():
        l.append(i)
for i in d:
    l.insert(i,d[i])
op="".join(l)
print(op)

