mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]%2!=0:
            mat[i][j]=mat[i][j]**2
        else:
            mat[i][j]=mat[i][j]**3
print(mat)

#list comprehension
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat=[[mat[i][j]**2 if mat[i][j]%2!=0 else mat[i][j]**3 for i in range(len(mat)) for j in range(len(mat[i]))]]
print(mat)

#using another list 
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)

#list comprehension 1D
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([ele**2 if ele%2!=0 else ele**3 for row in mat for ele in row])
#list comprehension 2D
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[ele**2 if ele%2!=0 else ele**3 for ele in row]for row in mat])
