"""
Page 79 - Cracking the coding interview
Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3, where a, b, c
and d are integers between 1 and 1000.
"""

def findSumOfCubes():
    data = {}
    for i in range(1, 1001):
        for j in range(1, 1001):
            result = i**3 + j**3
            if result in data:
                data[result].append((i, j))
            else:
                data[result] = [(i, j)]
    return data

if __name__ == "__main__":
    result = findSumOfCubes()
    count = 0
    for key, value in result.items():
        for val1 in value:
            for val2 in value:
                if val1[0] != val2[1] and val1[1] != val2[0] and val1[0] != val2[0] and val1[1] != val2[1]:
                    # print(val1, val2)
                    count += 1
    print(count)
