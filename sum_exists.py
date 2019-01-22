import random

from merge_sort import mergeSort


def checkSumofNumbers(dataList, num):
    i = 0
    j = len(dataList) - 1
    while(i < j):
        if (dataList[i] + dataList[j]) == num:
            return i, j
        elif (dataList[i] + dataList[j]) > num:
            j -= 1
        elif (dataList[i] + dataList[j]) < num:
            i += 1
    return None, None


if __name__ == "__main__":
    dataList = [-4, 40, 62, 39, 21, -61, 68, 31, 10, 1]
    dataList = mergeSort(dataList)
    num = 41
    print("Sorted list: {} search for sum: {}".format(dataList, num))
    result = checkSumofNumbers(dataList, num)
    print(result)
