import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # Check if the matrix is 1x1 or a 2x2 
        if self.h == 1:
            return self.g[0][0]
        else:                
            return (self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0])

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        # Check if the matrix is 1x1 or a 2x2 
        trace_result = 0
        
        for i in range(self.h):
            trace_result += self.g[i][i]
        
        return trace_result

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverseMat = []
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1:
            return  Matrix([[1/(self.g[0][0])]])
        elif self.h == 2:
            # If the matrix is 2x2, check that the matrix is invertible
            if self.determinant() == 0:
                raise ValueError('The matrix is not invertible.')
            else:
                # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]

                factor = 1 / self.determinant()

                inverseMat = [[d, -b],[-c, a]]

                for i in range(len(inverseMat)):
                    for j in range(len(inverseMat[0])):
                        inverseMat[i][j] = factor * inverseMat[i][j]

        return Matrix(inverseMat)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = zeroes(self.w,self.h)
        
        # Loop through the rows and columns and assign the values to transposed matrix
        for i in range(self.h):
            for j in range(self.w):
                transpose[j][i] = self.g[i][j]
         
        return transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]       

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        # Initialize an empty result array
        matrixSum = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrixSum[i][j] = self.g[i][j] + other.g[i][j]
        
        return matrixSum
            
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        # Initialize the result
        negative = zeroes(self.h,self.w)
        
        # Loop through the matrix and negate each element
        for i in range(self.h):
            for j in range(self.w):
                negative[i][j] = -self.g[i][j]         
        
        return negative

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        #   
        # TODO - your code here
        #
        # Initialize an empty result array
        matrixSub = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrixSub[i][j] = self.g[i][j] - other.g[i][j]
        
        return matrixSub

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "Matrices can only be multiplied if colA and rowB are the same")
        
        #   
        # TODO - your code here
        #       
        
        # Initialize an empty result array
        matrixMul = zeroes(self.h,other.w)
        
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    matrixMul[i][j] += self.g[i][k] * other.g[k][j]
        
        return matrixMul

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            
            #   
            # TODO - your code here
            #
            
            matrixResult = self
            
            # Loop through the matrix and multiply each element
            for i in range(self.h):
                for j in range(self.w):
                    matrixResult[i][j] *= other
                    
            return matrixResult
            