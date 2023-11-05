'''
Givena string, write a function to check if it is a permutation of a
palidrome. A palindrome is a word or phrase that is the same forwards and backwards.
A permuation is a rearrangement of letters. The palindrome does not need to be limited to
just dictionary words.
'''

'''
study:
there's only one character thats allowed to be unique
at a time:
* count the number of each character

if by adding 1 to a single odd count of a letter makes all counts even,
then the string is a palinedrome.



* count the number of odd counts.



There is only one count that's allowed to be odd in
a palindrome therefore, we return
whether there is more than 1 odd character count in
the given string.
'''

from collections import Counter

class Solution:
    def palindrome_permutation1(self, string):
        character_counter = Counter(string)
        odd_counts = sum([ character_counter[letter] % 2 for letter in character_counter ])
        answer = ((odd_counts==0) or (odd_counts==1))
        raise NotImplementedError
        return answer
