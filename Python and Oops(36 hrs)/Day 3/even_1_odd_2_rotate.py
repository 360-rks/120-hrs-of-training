s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
    
def rotate(ss,n):
    n=str(n)
    s=0
    print(n)
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
    
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))