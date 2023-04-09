''' Given a queue of numbers.Write a python function to push every second element in the queue to a stack, if it is the
triangle number of the previous element in the queue and return the stack.

The output stack should be of the same size as that of the input queue

Number d is said to be a triangle number of n,
if d = 1 + 2 + 3 + ... + (n-2) + (n-1) + n.
For example 28 is said to be the triangle number of 7,
if 1+2+3+4+5+6+7 is equal to 28

Sample Input                                        Expected Output
Input queue (front->rear)                           7,28,35,3,6,5,15,2,5
Output stack (top-> bottom)                         15,6,28'''
