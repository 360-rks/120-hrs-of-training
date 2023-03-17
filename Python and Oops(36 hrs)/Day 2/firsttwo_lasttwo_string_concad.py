def function1(str1):
    if(len(str1)<2):
        return -1
    else:
        return str1[0:2]+str1[-2:]
    
print(function1("w3resource"))
print(function1("w3"))
print(function1("A"))
