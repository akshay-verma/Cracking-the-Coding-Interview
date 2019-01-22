"""
Interview Questions 1.2 Page 90 Cracking the Coding Interview

Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""


def findSumOfString(string):
    total = 0
    for char in string:
        total += ord(char)
    return total


def checkPermutation(string1, string2):
    total1 = findSumOfString(string1)
    total2 = findSumOfString(string2)
    return total1 == total2


if __name__ == "__main__":
    string1 = "abcd"
    string2 = "dcba"
    result = checkPermutation(string1, string2)
    print(result)
