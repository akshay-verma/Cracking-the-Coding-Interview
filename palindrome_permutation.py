"""
Interview Questions 1.4 Page 91 Cracking the Coding Interview

1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

from itertools import permutations


def checkPalindromePermutation(string):
    data = {}
    for char in string:
        if char in data:
            data[char] += 1
        else:
            data[char] = 1
    count = 1
    for char in data:
        if data[char] == 1:
            if count > 1:
                return False
            count += 1
    return True


if __name__ == "__main__":
    string = "abcabc"
    for inputStr in permutations(string):
        inputStr = "".join(inputStr)
        result = checkPalindromePermutation(inputStr)
        print(inputStr, result)
