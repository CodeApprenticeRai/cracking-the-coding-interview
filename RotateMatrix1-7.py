'''
Given an image represented by an N*N matrix, where each pixel is 4 bytes.
Write a method to rotate the image by 90 degress. Can you do this in place.
This should be done in ipynb. 
'''

'''
Solution English:
update each row, writing it as it's corresponding columnar update

[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

copy [[1],  as  [1, 5, 9, 13]
      [5],
      [9],
      [13]
     ]

reverse [1,5,9,13] 

[
    [13,9,5,1],
    [14,10,6,2],
    [15,11.7,3],
    [16,12,8,4]
]

(0,0) -> (0,3),
(0,1) -> (1,3),
(0,2) -> (2,3),
(0,3) -> (2,3),

'''

from os import sep


class Solution:
    def __init__(self):
        pass
    
    def reverse_array(self, arr):
        temp = None
        index1 = 0
        index2 = len(arr)-index1-1

        while (index1 < index2): #if both indexors point to the same element no need to swap
            temp = arr[index1] #the -1 is becuase of zero indexing
            arr[index1] = arr[index2]
            arr[index2] = temp

            index1 += 1
            index2 -= 1

        return arr

    def rotate_matrix(self, matrix):
        copy_matrix = []

        if (len(matrix) > 0):
            #for each column in matrix 
            for j in range(len(matrix[0])): #!holds for an n by n matrix only
                #for each row in the matrix, starting with the last 
                copy_matrix_row = []
                for i in range(len(matrix)-1, -1, -1):
                    #write the last row in matrix and the first column of the matrix
                    copy_matrix_row.append(matrix[i][j])
                # copy_matrix_row = self.reverse_array(copy_matrix_row)
                copy_matrix.append(copy_matrix_row)
        return copy_matrix 

if __name__ == "__main__":
    #initailize Solution class and run algorithm
    data = [
        [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]
    ]

    example_array = [1,2,3,4,5]

    solver = Solution()
    # print( solver.reverse_array(example_array[:]), example_array[:][::-1], sep="\t" ) 
    print( data[0], solver.rotate_matrix(data[0]) , sep="\n\n")