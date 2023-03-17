dict1 = {"P":"Pediatrics","O":"Orthopedics","E":"ENT"}

def patients_max(list1):
    for i in list1:
        k=list1.count('P')
        l=list1.count('O')
        q=list1.count('E')
    if(k>l and k>q):
        print(dict1["P"])
    elif(l>k and l>q):
        print(dict1["O"])
    else:
        print(dict1["E"])
        
patients_max([101,'P',102,'O',302,'P',305,'P'])
patients_max([101,'O',102,'O',302,'P',305,'E',401,'O',656,'O'])
patients_max([101,'O',102,'E',302,'P',305,'P',401,'E',656,'O',987,'E'])
