'''
Write a method to replace all spaces in achar_array with %20.
You may assume that the givenchar_array has sufficient space at the end to hold
the additional characters, and that you are given the "true"
length of thechar_array. (Note: if implementing in Java, please use a character array
so that you can perform this operation in place).
'''
import copy

class Solution:
    def urlify(self, char_array, array_length):
        copy_string = ""
        for character in char_array:
            if character == " ":
                copy_string += "%20"
            else:
                copy_string += character
        i=0
        while (i < array_length):
            char_array[i] = copy_string[i]
            i += 1
        while (i < len(copy_string)):
            char_array.append(copy_string[i])
            i += 1
        return char_array

if __name__ == "__main__":
    solver = Solution()
    print("Running tests: (all should be True)")
    test_strings = ["hello world", "helloworld"]
    test_char_arrays = [list(string) for string in test_strings]
    test_cases = [(char_array, copy.copy(char_array), len(char_array)) for char_array in test_char_arrays]
    for char_array_original, char_array, array_length in test_cases:
        recast_string = "".join(solver.urlify(char_array, array_length))
        recast_original_string = "".join(char_array_original)
        print(recast_original_string, recast_string, sep="\t")
