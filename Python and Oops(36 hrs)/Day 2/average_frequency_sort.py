def find_more_than_average(marks):
    average = sum(marks)/10
    count=0
    for i in marks:
        if(i>average):
            count+=1
    return count*10 

def generate_frequency(marks):
    list1=[]
    for i in range(26):
        list1.append(marks.count(i))
    return list1

def sort_marks(marks): 
    a=[]
    a=list(marks)
    a.sort()
    return a
  

print(find_more_than_average([12,18,25,24,2,5,18,20,20,21]))
print(generate_frequency([12,18,25,24,2,5,18,20,20,21]))
print(sort_marks([12,18,25,24,2,5,18,20,20,21]))
