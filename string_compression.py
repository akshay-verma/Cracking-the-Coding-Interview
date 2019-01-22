"""
Page 91 - Cracking the Coding Interview

1.6 String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def compressString(string):
    prevIndex = 0
    newStr = []
    count = 1
    index = 1
    while index <= len(string):
        newStr.append(string[prevIndex])
        if index < len(string) and string[index] == string[prevIndex]:
            count += 1
            prevIndex += 1
            index += 1
        else:
            newStr.append(str(count))
            count = 1
            prevIndex = index
            index += 1
    return "".join(newStr)

if __name__ == "__main__":
    inputStr = "aaaaabbccddeeffgghh"
    compressedStr = compressString(inputStr)
    print(compressedStr)
