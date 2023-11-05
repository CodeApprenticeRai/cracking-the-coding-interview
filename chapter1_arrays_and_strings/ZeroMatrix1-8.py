'''
Write an algorithm such that if an element in an MxN matrix is 0 it's entire row and column are set to 0.
'''

class Solution:
    def zero_matrix(self, matrix):
        #if the matrix is empty just return it
        if not matrix:
            return matrix

        self.ZERO_ROW = [ 0 for j in range(len(matrix[0]))] #this is a constant

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    matrix[i] = self.ZERO_ROW
                    break
        
        return matrix

if __name__=="__main__":
    data = [
        [
            [1,2,3,4],
            [5,6,7,8],
            [0,10,11,12],
            [13,14,15,16]
        ]
    ]

    solver = Solution()
    print( solver.zero_matrix(data[0]) )