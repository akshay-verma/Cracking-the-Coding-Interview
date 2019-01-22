"""
Page 81 - Cracking the Coding Interview
Given a smaller strings and a bigger string b, design an algorithm to find all permutations
of the shorter string within the longer one. Print the location of each permutation.
"""

def findSubstringWithPermutation(string1, string2):
    string1Map = {}
    for c in string1:
        if c in string1Map:
            string1Map[c] += 1
        else:
            string1Map[c] = 1
    for index in range(0, len(string2) - len(string1) + 1):
        tmpCopy = string1Map.copy()
        substr = string2[index:index + len(string1)]
        count = 0
        for c in substr:
            if c in tmpCopy:
                tmpCopy[c] -= 1
        if check(tmpCopy):
            print(index, substr)


def check(stringMap):
    for c in stringMap.values():
        if c != 0:
            return False
    return True


if __name__ == "__main__":
    # string1 = "abbc"
    # string2 = "cbabadcbbabbcbabaabccbabc"
    string1 = "aaaa"
    string2 = "aaaabbbbbbbbbbaaaa"
    findSubstringWithPermutation(string1, string2)
