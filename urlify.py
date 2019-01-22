"""
Interview Questions 1.3 Page 90 Cracking the Coding Interview

URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith", 13
Output: "Mr%20John%20Smith"
"""


def createURL(string):
    newStr = []
    for char in string:
        if char != " ":
            newStr.append(char)
        else:
            newStr.append("%20")
    return "".join(newStr)


def createURLInPlace(string):
    string = list(string)
    for idx in range(len(string)):
        if string[idx] == " ":
            string[idx] = "%20"
    return "".join(string)


if __name__ == "__main__":
    string = "Mr John Smith"
    url = createURL(string)
    print(url)
    url = createURLInPlace(string)
    print(url)
