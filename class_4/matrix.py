# mat_A=[[1,2,3],[4,5,6],[7,8,9]]
# mat_B=[[10,11,12],[13,14,15],[16,17,18]]
# print(mat_A)
# print(mat_B)
# print(mat_B[1])
# print(mat_B[1][2])

#add two matrix
mat_A=[[1,2,3],[4,5,6],[7,8,9]]
mat_B=[[10,11,12],[13,14,15],[16,17,18]]
mat_result=[[0,0,0],[0,0,0],[0,0,0]]
for i in (range(len(mat_A))):
    for j in (range(len(mat_A[0]))):
        mat_result[i][j]=mat_A[i][j]+mat_B[i][j]
print(mat_result)

