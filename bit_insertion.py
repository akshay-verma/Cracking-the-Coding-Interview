"""
Page 115 - Cracking the Coding Interview

5.1 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE
Input: N 10000000000, M = 10011, i 2, j 6
Output: N = 10001001100
"""


def numberInsert(num1, num2, i, j):
    num1Len = len(num1)
    num2Len = len(num2)
    if num2Len > num1Len:
        raise ValueError("Bits in second number greater than first")
    if num2Len == num1Len:
        return num2
    diff = num1Len - j
    temp = ""
    for idx in range(diff - 1):
        temp += "0"
    temp += num2
    for idx in range(i):
        temp += "0"
    num2 = temp
    temp = ""
    for idx in range(num1Len):
        temp += str(int(num1[idx]) | int(num2[idx]))
    return temp


if __name__ == "__main__":
    N = "10000000000"
    M = "10011"
    result = numberInsert(N, M, 2, 6)
    print(result)
    print("Check if successfully inserted...")
    print()
