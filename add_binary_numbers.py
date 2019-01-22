"""
2.1-4
Consider the problem of adding two n-bit binary integers, stored in two n-element
arrays A and B. The sum of the two integers should be stored in binary form in
an (n+1)-element array C. State the problem formally and write pseudocode for
adding the two integers.
"""


def addBinaryNumbers(firstNum, secondNum):
    residue = 0
    result = ""
    for index in range(len(firstNum) - 1, -1, -1):
        num1 = firstNum[index]
        num2 = secondNum[index]
        res = int(num1) + int(num2) + residue
        if res == 2:
            res = 0
            residue = 1
        elif res == 3:
            res = 1
            residue = 1
        result = str(res) + str(result)
    result = str(residue) + str(result)
    return result


def convertDecimalToBinary(number):
    quotient = number // 2
    remainder = number % 2
    result = str(remainder)
    while True:
        quotient = number // 2
        remainder = number % 2
        result = str(remainder) + str(result)
        if quotient == 1:
            break
        number = quotient
    return result


def convertBinaryToDecimal(number):
    result = 0
    pos = 0
    for index in range(len(number) - 1, -1, -1):
        result += 2**pos * int(number[index])
        pos += 1
    return result


if __name__ == "__main__":
    print(convertBinaryToDecimal(addBinaryNumbers("1111", "1111")))
