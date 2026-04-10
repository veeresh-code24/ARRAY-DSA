# 

'''class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        def row(i):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

        

        def column(j):
            for i in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

            
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row(i)
                    column(j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

# Better

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])
        row = [0] * n
        column = [0] * m


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1

        for i in range(n):
            for j in range(m):
                if row[i] == 1 or column[j] == 1:
                    matrix[i][j] = 0

# optimal

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        col0 = 1

        # Step 1: Mark rows and columns
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Update matrix (reverse order)
        for i in range(n-1, -1, -1):
            for j in range(m-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if col0 == 0:
                matrix[i][0] = 0'''






