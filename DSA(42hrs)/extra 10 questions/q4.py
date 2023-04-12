"""
Question 4
'''
Consider that the human tower is to be performed on a stage
and the stage has a maximum weight limit.
Write a python program to find the maximum number of people
at the base level such that the total weight of tower does
not exceed the 
maximum weight limit of the stage.
Assume that:
1. Each person weighs 50 kg
2. There will always be odd number of men at the base level
of the human tower.
'''
"""

wl=int(input("weight limit of stage "))
epw=50
npa=wl//epw
sum=0
for i in range(npa):
    if sum<wl:
        sum=sum+i*epw
    if sum>=wl:
        i-=1
        break
if i==0:
    npab=0
elif i%2==0:
    npab= i-1
else:
    npab= i
print("max number of people at base = ",npab)
#extra
print("tower looks like:")
for i in range(1,npab+1):
    print(" "*(npab-i),end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()
              
