"""
Interview Questions 1.1 Page 90 Cracking the Coding Interview

Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

def checkUniqueCharsInString(string):
    """
    Time complexity: O(N)
    """
    data = {}
    for char in string:
        if char in data:
            return False
        else:
            data[char] = 1
    return True


def checkUniqueCharsInString(string):
    """
    Time complexity: O(N^2)
    """
    for idx1 in range(0, len(string)):
        for idx2 in range(0, len(string)):
            if idx1 != idx2:
                if string[idx1] == string[idx2]:
                    return False
    return True


def checkUniqueCharsInString(string):
    """
    Time complexity: O(N * log N)
    """
    string = sorted(string)
    for idx in range(0, len(string) - 1):
        if string[idx] == string[idx + 1]:
            return False
    return True


if __name__ == "__main__":
    inputStr = "abcdefghijkla"
    result = checkUniqueCharsInString(inputStr)
    print(result)
