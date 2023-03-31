'''Given two lists,both having String elements, write a python program using python lists to create a new string as per the
rule given below:
    
The first element in list1 should be merged with last element in list2, second element in list1 should be merged with
second last element in list2 and so on. If an element in list1/list2 is None, then the corresponding element in the other
list should be kept as it is in the merged list.

Sample Input
list1=['A','app','a','d','ke','th','doc','awa']
list2=['y','tor','e','eps','ay',None,'le','n']

Expected Output
"An apple a day keeps doctor away"

'''
list1 = list(input().split(","))
list2 = list(input().split(","))
list2.reverse()
merged_list = []
for i, elem in enumerate(list1):
    if list2[i] is None:
        merged_list.append(elem)
    else:
        merged_list.append(elem + list2[i])
result = ' '.join(merged_list)

print(result)  
