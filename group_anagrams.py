"""
Page 150 - Cracking the Coding Interview

10.2 Group Anagrams: Write a method to sort an array ot strings so that all tne anagrnms are next to
each other.
"""

from radix_sort import _sort, getDataListFromIndex


def groupAnagrams(dataList):
    counter = {}
    for index, data in enumerate(dataList):
        total = 0
        for char in data:
            total += ord(char)
        if total in counter:
            counter[total].append(index)
        else:
            counter[total] = [index]
    data = [0] * len(dataList)
    count = 0
    for key, values in counter.items():
        if values:
            for val in values:
                data[val] = count
        count += 1
    indexList = _sort(data, 1)
    return getDataListFromIndex(dataList, indexList)


if __name__ == "__main__":
    dataList = ["ddl, ""abc", "pqr", "prq", "dad", "bac", "dda", "aaa", "aaa", "dld"]
    result = groupAnagrams(dataList)
    print(result)
