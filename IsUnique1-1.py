'''
Implement an algorithm to determine if a string has all unique characters.
What is you cannot use additional data structures?
'''

class Solution:
    def is_unique(self, string):
        cache = set()
        for letter in string:
            if letter not in cache:
                cache.add(letter)
            else:
                return False
        return True
