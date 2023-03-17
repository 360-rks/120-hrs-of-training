#question 
number = int(input("Enter a numnber:"))
if(number%5==0 and number%3==0):
    print("Number is multiple of both")
elif(number % 3==0):
    print("Number is multiple of 3")
elif(number%5==0):
    print("Number is multiple of 5")
else:
    print("Invalid")
    
