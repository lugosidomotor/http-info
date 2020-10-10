# Function to print the matrix 
def printMatrix( mat ): 
      
    for i in range(0, len(mat)):     
        for j in range(0, len(mat)): 
              
            print (mat[i][j], end = ' ') 
        print ("") 
test = [ [1, 2, 3 ], 
        [4, 5, 6 ], 
        [7, 8, 9 ] ] 
def transposeMatrix(mat):
    for i in range(0,len(mat)):
        for j in range(i,len(mat)):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
def reverseColums(mat):
    k = len(mat)-1
    for i in range(0,len(mat)):
       for j in range(0,k):
            temp = mat[j][i]
            mat[j][i] = mat[k][i]
            mat[k][i] = temp
            k = k - 1
print(len(test))
transposeMatrix(test)
reverseColums(test)
printMatrix(test)
