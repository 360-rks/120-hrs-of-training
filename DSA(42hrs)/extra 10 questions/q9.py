"""
Question 9
Write a python program that it should consist of special charnumbers and chars. 
if there are even numbers of special chars Then the series should start with even followed by odd
Input: 19@a42&516
Output: 492561
If there are odd numbers of special chars then the output will be starting with odd followed by even
Input: 5u6@25g7#@
Output: 56527
If there are any number of additional digits append them at
 last
"""

s="5u6@25g7#@"
counter=0
digits=[]
for i in s:
    if i.isalnum()==False:
        counter+=1
    if i.isdigit():
        digits.append(i)
digits=list(map(int,digits))
digitso=list(filter(lambda x:x%2!=0,digits))
digitse=list(filter(lambda x:x%2==0,digits))
op=""
if counter%2==0:
    for i in range(len(digits)):
        if i%2==0 and len(digitse)!=0:
            op=op+str(digitse.pop(0))
        else:
            op=op+str(digitso.pop(0))
else:
    for i in range(len(digits)):
        if i%2==0 and len(digitso)!=0:
            op=op+str(digitso.pop(0))
        else:
            op=op+str(digitse.pop(0))

print(op)