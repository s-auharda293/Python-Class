mat_A=[[2,3,5],
       [4,5,6],
       [7,8,9]]
mat_B=[[2,1,],
       [3,5],
       ]
mat_C=[[0,0],
       [0,0]]
for i in range(len(mat_C)):
    for j in range(len(mat_C)):
        mat_C[i][j]=mat_A[i][0]*mat_B[0][j]+mat_A[i][1]*mat_B[1][j]
print(mat_C)
