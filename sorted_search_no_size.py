"""
10.4 Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt ( i) method that returns the element at index i in
0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
"""


def findStartAndEnd(dataList, value):
    index = 1
    while elementAt(dataList, index) != -1 and dataList[index] < value:
        index = index * 2
    return index // 2, index


def elementAt(dataList, index):
    try:
        return dataList[index]
    except IndexError:
        return -1


def sortedSearchNoSize(dataList, value):
    start, end = findStartAndEnd(dataList, value)
    while (start <= end):
        mid = (start + end) // 2
        if elementAt(dataList, mid) == value:
            return mid
        elif elementAt(dataList, mid) > value or elementAt(dataList, mid) == -1:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == "__main__":
    dataList = [1, 5, 8, 10, 12, 18, 21, 30, 42, 50]
    result = sortedSearchNoSize(dataList, 50)
    print(result)
