"""Question 5
 Parenthesis matching
A non empty string instr containing only parenthesis (,),{.},[,] it return outstr based on following,
– instr is properly nested and return 0
– instr not properly nested, return position of element in instr
– position start from 1
Input: {([])} Output: 0
Input: (])()] Output: 2
Input: [[()]  Output: n+1 for last element i.e 5+1=6
"""
def parenthesis_check(instr):
    stack=[]
    for i in range(len(instr)):
        if instr[i] in '({[':
            stack.append(instr[i])
        else:
            top=stack.pop()
            if instr[i]==")" and top!="(":
                return i+1
            elif instr[i] == '}' and top != '{':
                return i + 1
            elif instr[i] == ']' and top != '[':
                return i + 1
    if stack:
        return len(instr) + 1
    else:
        return 0
instr="{([])}"
print(parenthesis_check(instr))
print("--------------------------------")
instr="(])()]"
print(parenthesis_check(instr))
print("--------------------------------")
instr="[[()]"
print(parenthesis_check(instr))
print("--------------------------------")