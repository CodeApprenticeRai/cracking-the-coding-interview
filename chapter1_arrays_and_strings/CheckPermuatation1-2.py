'''
1.1. Check Permutation: Given two strings, write a method
to decide if one is a permutation of the other
'''


# '''
# way too much code
# '''
# class Counter:
#     def __init__(self):
#         self.counter = {}
#
#     def add(self, item):
#         if itm in self.counter:
#             self.counter[item] += 1
#         else:
#             self.counter[item] = 1
#         return None
#
#     def get(self, item):
#         if item in self.counter:
#             return (item, self.counter[item])
#         else:
#             raise IndexError

from collections import Counter

class Solution:
    def check_permutation(self, string1, string2):
        if (len(string1) != len(string2)):
            return False
        else:
            string_length = len(string1)
            counter1 = Counter(string1)
            counter2 = Counter(string2)
            return counter1 == counter2


if __name__ == "__main__":
    import sys
    # print(sys.argv)
    # if ((len(sys.argv) > 1) and (sys.argv[1] == "--test")):
    #     if (sys.argv[2]=="Counter"):
    #         counter = Counter()
    #         counter.get("j")
    #     else:
    #do tests
    solver = Solution()
    print("Running tests: (all should be True)")
    print( solver.check_permutation("hello", "olloh") == False )
    print( solver.check_permutation("hello", "hollo") == False )
    print( solver.check_permutation("hello", "olleh") == True )
