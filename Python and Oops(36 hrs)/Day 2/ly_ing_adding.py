def function1(str1):
    if(len(str1)<3):
        print(str1)
    elif(str1[-3:]=="ing"):
        print(str1+"ly")
    else:
        print(str1+"ing")

function1("sleep")
function1("amazing")
function1("is")