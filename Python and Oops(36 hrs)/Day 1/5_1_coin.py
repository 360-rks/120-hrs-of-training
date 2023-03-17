def mincoin(x,y,z):
    if(x*5+y*1<z):
        print(-1)
    else:
        n1=z//5
        n2=z%5
        print("5=",n1,"\n1=",n2)
    
x=int(input("5="))
y=int(input("1="))
z=int(input("amt="))
mincoin(x,y,z)