'''
Assume you have a method isSubstring which checks if one word is
a substring of another. 
Given two strings s1 and s2, write code to check if s2 is a rotaion of s1
using only one call to isSubstring
'''

#checks if string1 is a substring of string2.
from msilib.schema import Error

from tomlkit import string


def is_substring(string1, string2):
    temp = None
    if (len(string1) > len(string2)):
        raise Error("string1 must be shorter length than string2") 

    for i in range(len(string1)):
        if (string1[i]!=string2[i]):
            return False
    return True

class Solution:
    def string_rotation(self, string1, string2):
        string_length = len(string1)

        if (string_length == len(string2)):
            string1_doubled = string1 + string1
            return string2 in string1_doubled
        else:
            return False

if __name__ == "__main__":
    print( is_substring("water", "watermelon") )
    print( is_substring("watre", "watermelon") == False )
    
    solver = Solution()
    print( solver.string_rotation("waterbottle", "erbottlewat") == True )


'''
becuase string2 is expected to be a rotation of string1
it will be comtained in the doubled string1. 
This is a general property of rotated strings.
'''