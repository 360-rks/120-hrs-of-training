def translate(dicto,list1):
    list2=[]
    for i in list1:
        list2.append(dicto[i])
    return list2
    

dicto={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1 = ["merry","christmas"]
print(translate(dicto,list1))