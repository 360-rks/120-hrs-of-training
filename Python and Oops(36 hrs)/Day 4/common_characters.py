string1= input()
string1 = string1.replace(" ","")
string2 = input()
string1 = string1.replace(" ","")
l=[]
for i in string1:
    for j in string2:
        if(i==j):
            l.append(i)
            break


l = set(l)
for i in l:
    print(i,end="")
if list(l)==[]:
    print(-1)

