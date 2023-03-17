num = int(input())
x=True
while(x):
    temp= str(num+1)
    if temp==temp[::-1]:
        x=False
    num+=1
print(int(temp))


#2nd method
import sys
def Next_smallest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
        
print(Next_smallest_palindrome(99))
print(Next_smallest_palindrome(1221))