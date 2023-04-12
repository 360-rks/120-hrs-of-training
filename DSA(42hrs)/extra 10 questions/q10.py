"""
Question 10
Password generation
Given input of array of string in format <emnp name> <emp number> separated by comas ,Emp
should contain only alphabets and employee number. You have to generate password for
Ex:
input: Robert: 36787, Tina: 68721, Jo:56389
Output: tiX
Conditions: len of robert is 6 and 6 is present in emp number
robert (36787), so return the alphabet at position 6 that is t.
Now len of tina is 4 and 3 is not present in the 68721 so select the number which is max 
and less than the len of tina so select 2 return the alphabet that is at position 2 that is i.
Now In of Jo is 2 it is not present in 56389 and there is not present any number 
which is less than 2 so return X.
"""

def generate_password(input_str):
    password = ''
    for emp in input_str.split(', '):
        name, number = emp.split(': ')
        name_len = len(name)
        max_num = 0
        for d in number:
            if d.isdigit() and int(d) < name_len and int(d) > max_num:
                max_num = int(d)
        if str(name_len) in number:
            password += name[name_len - 1]
        elif max_num == 0:
            password += 'X'
        else:
            password += name[max_num - 1]
    return password

print(generate_password("Robert: 36787, Tina: 68721, Jo: 56389"))