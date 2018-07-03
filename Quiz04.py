def ischeckvec(vector):

  '''
  Input
  vector that is 1 x n

  Output
  True or false

  This function checks each element of the vector to see if its a number.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  return inputStatus

def ischeckmat(matrix):
  '''
  Input 
  matrix n x m

  Output
  true or false

  This function checks each row of the matrix and runs it through ischeckvec to make sure the row is number and then iterates through each row
  '''
  inputStatus = True

  for j in range(len(matrix)):
    if ischeckvec(matrix[j]) != True:
      inputStatus = False
      print("Invalid Input")
  return inputStatus    
  
def dot(vector01,vector02):
  '''
  Inputs
    vector01 should be 1 x n in length
    vector02 should be 1 x n in length

  Output should be a scalar

  This function compares the lengths of two vectors together.  
  If they are the same length it multiolies the first column of vector01 by the first column of vector02.
  Next it takes this value and stores it in the out container.  
  it repeats this multiplication for each column and adds the products together inside of the out container.
    '''

  
  if ischeckvec(vector01) == True and ischeckvec(vector02) and len(vector01)==len(vector02) and len(vector01)!=0:
    result = 0#checks to see that the two vectors are the same length and the second vector is not 0

    out = 0 # starts the holding array at 0
    for k in range(len(vector01)):
        out += vector01[k] * vector02[k]# for each iteration after the product is done it adds the number into the container out
    return out
  else:
    print("input invalid")

def vecSubtract(vector01,vector02):

  '''
  Inputs
  vector01 should be 1 x n in length
  vector02 should be a 1 x n in length
  
  Output 
  newvec should be a 1 x n vector
  

  In the vecSubtract function two vector lengths are compared, if they are the same length then they can be subtracted.
  Each element from their respective places in each row is subtracted from each other then returned into a new vector containing the result.

  '''

  if ischeckvec(vector01) == True and ischeckvec(vector02) and len(vector01)==len(vector02) and len(vector01)!=0:
    result = 0#checks to see that the two vectors are the same length and the second vector is not 0

    # checks to see that the vectors are the same length
    newvec = []
    for i in range(len(vector01)):
      newvec.append(vector01[i] - vector02[i])# for each iteration each vector is subtracted from one another and put into newvec
    return newvec
  else:
    print("invalid inputs")

def scalarVecMulti(scalar,vector):

  '''
  Input
  scalar should be a number
  vector should be a 1 x n in length
  
  Output
  newvector should be a 1 x n in length

  This function inputs a scalar and a vector, then multiplies the scalar to every element in the vector for the length of the vector.
  The loop iterates for the range of the vector, each iteration the scalar is multiplied by the scalar.
  '''

  
  # If the input is valid the function continues to compute the scalar times vector multiplication
  if ischeckvec(vector) == True:
    result = 0
  
    newvector = []

    for i in range(len(vector)):
      newvector.append(scalar * vector[i])
    # for each iteration the vector element is multiplied by the scalar and put into the new vector
    return newvector
  
def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the 2-norm
  if inputStatus == True:
    result = 0


  # This for loop will compute the sum of the squares of the elements of the vector. 
    for i in range(len(vector)):
      result = result + (vector[i]**2)
    result = result**(1/2)
    return result

def matVec(matrix,vector):
  '''
  Inputs:
    A- matrix with dimensions row-matrix x column-matrix
    B- matrix with dimensions row-vector x 1
  Output:
    C - matrix with dimensions row-matrix x 1
  Details:
    This is the matrix times vector multiplication algorithm.
    For each matrix row, each vector columns = 1, and con to 0. con is the placeholder matrix to add each repition. Then for each matrix     column, add matrix[i][k]*vector[k] to con. Then set container[i][1] = con.
    The result is a Matrix rows in the matrix by 1.
  '''
  if ischeckmat(matrix) == True:
    if ischeckvec(vector) == True:
      rA = len(matrix)# find the number of rows in matrix A
      cA = len(matrix[0])# find the number of columns in matrix A
      rB = len(vector)# find the number of rows in vector B


      #initialize a container to be a matrix  with 0s for all entries.
      container = [[0]*1 for row in range(rA)]


      for i in range(rA):
        # iterate through rows of the matrix
        # iterate through columns of vector whish should be 1
        con= 0
        for k in range(cA):
          #iterate through columns of the matrix
          con +=  matrix[i][k]*vector[k]
          #use += to add con + calculated value to placeholder matrix
        container[i] = con #final matrix will be the number of rows by 1 column
      return container

def transposeMat(matrix):

  '''
  Input
  matrix is n x m dimensions
  Output
  matrix is m x n dimensions

  This function swaps the rows as columns and the columns as rows
  '''
  if ischeckmat(matrix) == True:


    rA = len(matrix) # number of rows in the matrix
    cA = len(matrix[0]) # number of columns in the matrix

  
    container = [[0]*rA for i in range(cA)]
    # starts an empty container with dimensions of the flipped matrix

    for i in range(rA):
      
      for j in range(cA):
        
        container[j][i] = matrix[i][j]

    return container

def QRFactor(matrix):

  '''
  Input
  matrix is a n x m matrix input that is a list of columns

  Outputs
  matrix Q is a n x m matrix
  matrix R is a m x m upper triangular matrix
  
  The gram-Schmidt algorithm take column vectors in a matrix and produces orthonormal vectors. 
  The projections Q anr R are subtracted from the original matrix.
  

  '''
  if ischeckmat(matrix) == True:
  
    cA = len(matrix)# find number of rows in matrix
    rA = len(matrix[0]) # find the number of columns in matrix


    Qcontainer = [[0] * rA for row in range(cA)]
    Rcontainer = [[0] * cA for row in range(cA)]
    # when multiplying the dimensions of r need to match with q


  
    # everything is indexed via the columns of the input matrix
    for i in range(cA):
      
      Rcontainer[i][i]= twoNorm(matrix[i])
      #normalize Qcontainer
      rsub = 1 / Rcontainer[i][i]

      Qcontainer[i] = scalarVecMulti(rsub,matrix[i])
      
      for j in range(i+1,cA):

        Rcontainer[j][i] = dot(Qcontainer[i],matrix[j])

        m = scalarVecMulti(Rcontainer[i][j],Qcontainer[i])

        matrix[j] = vecSubtract(matrix[j],m)
        # subtrace the projections made by m
    return [Qcontainer,Rcontainer]
