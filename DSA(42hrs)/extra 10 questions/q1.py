"""
Question 1
'''
Write a python lambda expression for calculating simple interest.
If simple interest is greater than 1000, display as “Platinum Member”, 
otherwise “Gold Member”.
Use the below formula to calculate the simple interest.
simple_interest=(principal_amount*duration in years*rate_of_interest)/100
'''
"""
principal_amount,duration,rate_of_interest=input().split()
x=lambda pa,d,r:(int(pa)*int(d)*int(r))/100
result=x(principal_amount,duration,rate_of_interest)
print(result)
if result >1000:
    print("Platinum Member")
else:
    print("Gold Member")
