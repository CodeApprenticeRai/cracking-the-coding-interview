'''
Given a string, 
produce all rotations of that string:
"water" -> 
[
    "rwate", # d=1 
    "erwat", # d=2
    "terwa", # d=3
    "aterw", # d=4
    "water"  # d=0
] 
'''

'''

'''

class Solution:
    def rotate_array(self, array, d):
        n = len(array)
        return [array[(i % n)] for i in range(n-d, n-d+n, 1)]

    def all_rotations(self, array):
        n = len(array)
        new_arrays = []
        for d in range(len(array)):
            new_array = [array[(i % n)] for i in range(n-d, n-d+n, 1)] 
            new_arrays.append(new_array)
        return new_arrays

if __name__=="__main__":
    solver = Solution()
    example_char_array = [char for char in "water"]
    print( "".join(solver.rotate_array(example_char_array   , 1)) == "rwate"  ) 
    print( solver.all_rotations(example_char_array, ) )