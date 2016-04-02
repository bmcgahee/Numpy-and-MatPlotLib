#Author: Ben McGahee
#Title:  Matrices and Inverses
#Date: 4/2/2016
#Purpose: These functions determine whether a square matrix has an inverse or if 
#two square matrices are inverses of each other.
#A couple of tests are done for each function below.

import numpy as py
from numpy.linalg import inv

#hasInverse() determines if the square matrix has an inverse.
def hasInverse(matrixA):
    det_MatrixA = py.linalg.det(matrixA)
    if det_MatrixA != 0:
        return True
    else:
        return False

#isInverse() determines if two square matrices are inverses of each other.
def isInverse(matrixA, matrixB):
    A = matrixA
    B = matrixB
    C = inv(A)
    return py.allclose(B, C) #Determines if inverse of A is equal to B.

#TestA hasInverse(): The determinant of matrix is 0, so it has no inverse.
#Expected result is False.
matrixA = [[1, 2], [2, 4]]
inverseTestA = hasInverse(matrixA)
print inverseTestA
if inverseTestA == True:
    print "Matrix is non-singular, so it does has an inverse."
else:
    print "Matrix is singular, so it does not have an inverse."

#TestB hasInverse(): The determinant of matrix is non-zero, so it has an inverse.
#Expected result is True.
matrixB = [[1, 2], [3, 4]]
inverseTestB = hasInverse(matrixB)
print inverseTestB
if inverseTestB == True:
    print "Matrix is non-singular, so it does has an inverse."
else:
    print "Matrix is singular, so it does not have an inverse."

#Test1 isInverse(): AB = I, so expected result is True.
matrixA = [[1, 1],[ 2, 3]]
matrixB = [[3, -1], [-2, 1]]
inverseTestOne = isInverse(matrixA, matrixB)
print inverseTestOne
if inverseTestOne == True:
    print "The two matrices are inverses of each other."
else:
    print "The two matrices are not inverses of each other."

#Test2 isInverse(): CD is not I, so expected result is False.
matrixC = [[2, 4], [3, 1]]
matrixD = [[-1, 2], [-2, 5]]
inverseTestTwo = isInverse(matrixC, matrixD)
print inverseTestTwo
if inverseTestTwo == True:
    print "The two matrices are inverses of each other."
else:
    print "The two matrices are not inverses of each other."



