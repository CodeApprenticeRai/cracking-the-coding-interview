'''
Implement a method to perform basic string compression using the
counts of repeated characters. For example, the string aaabcccccaa would become
a2b1c5a3. If the compressed string would not become smaller than the original
string your method should reutrn the original string.
You can assume that the string has only uppercase and lowercase letters (a-z).
'''
import pdb

class Solution:
    def string_compression(self, string):
        raise NotImplementedError
        new_string = ""
        counter = 1
        active_char = ""
        for i in range(len(string)):
            if ((active_char=="") or (active_char==string[i])):#if we dont encounter a new letter
                counter += 1
            else:
                new_string += active_char
                new_string += str(counter)
                counter = 1
            active_char = string[i]
        if (len(new_string) > len(string)):
            return string
        else:
            return new_string

if __name__ == "__main__":
    solver = Solution()
    print("Running tests: (all should be True)")
    print( solver.string_compression("aabcccccaaa"), "a2b1c5a3", sep="\t" )
    print( solver.string_compression("a"), "a", sep="\t"  )
    print( solver.string_compression("abc"), "abc", sep="\t" )
