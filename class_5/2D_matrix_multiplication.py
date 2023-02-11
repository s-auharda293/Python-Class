# mat_C[i][j]=mat_A[i][0]*mat_B[0][j]+mat_A[i][1]*mat_B[1][j]
# mat_A=[[2,3],
#        [4,5]]
# mat_B=[[2,1],
#        [3,5]]
# mat_C=[[0,0],
#        [0,0]]
# check1=0
# check2=0
# for checkA in range(len(mat_A)):
#        check1=check1+1
# for checkB in range(len(mat_B)):
#        check2=check2+1
# if(checkA!=checkB):
#        print("The matrix cannot be multiplied.")
# else:
#        for i in range(len(mat_C)):
#               for j in range(len(mat_C)):
                     
#                      mat_C[i][j]=mat_A[i][0]*mat_B[0][j]+mat_A[i][1]*mat_B[1][j]
# print(mat_C)

mat_A=[[2,3],
       [4,5]]
mat_B=[[2,1],
       [3,5]]
mat_C=[[0,0],
       [0,0]]
for i in range(len(mat_A)):
       for j in range(len(mat_A[0])):
              for k in range(len(mat_A)):
                     mat_C[i][j] += mat_A[i][k] * mat_B[k][j]
print(mat_C)
