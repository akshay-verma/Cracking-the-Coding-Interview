"""
Page 149 - Cracking the Coding Interview

10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""


def shift(numList, index):
    temp = numList[index]
    for idx in range(index, len(numList) - 1):
        ptemp = numList[idx + 1]
        numList[idx + 1] = temp
        temp = ptemp
    return numList


def mergeSortedArray(list1, list2):
    i = j = 0
    while list1[i] is not None and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        else:
            list1 = shift(list1, i)
            list1[i] = list2[j]
            j += 1
            i += 1
    while j < len(list2):
        list1[i] = list2[j]
        j += 1
        i += 1
    return list1


if __name__ == "__main__":
    list1 = [0, 1, 2, 3, 7, 11]
    list2 = [1, 2, 5, 7, 8, 9]
    list1.extend([None] * len(list2))
    result = mergeSortedArray(list1, list2)
    print(result)
