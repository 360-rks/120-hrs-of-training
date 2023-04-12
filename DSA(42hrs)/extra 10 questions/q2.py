'''
Question 2
Write a python lambda expression for the following:
1. Find the modulo of two numbers and add it to the difference of the same two numbers.
2. Find the square root of a number using math library built-in function.
3. Find the square root of a number without using built-in function.
'''
from math import sqrt
n1=16
n2=10
a=lambda n1,n2:(n1%n2)+(n1-n2)
b=lambda n:sqrt(n)
c=lambda n:n**(1/2)
print(a(n1,n2))
print(b(n1))
print(c(n1))