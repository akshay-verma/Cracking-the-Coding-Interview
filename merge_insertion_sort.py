import random
import time

from insertion_sort import insertionSort


def mergeInsertionSort(dataList, reverse=False):
    if len(dataList) > 1:
        if len(dataList) < 25:
            dataList = insertionSort(dataList)
        else:
            mid = len(dataList) // 2
            leftData = dataList[:mid]
            rightData = dataList[mid:]
            mergeInsertionSort(leftData)
            mergeInsertionSort(rightData)
            leftIndex = rightIndex = 0
            for index in range(0, len(dataList)):
                if leftIndex >= len(leftData) or rightIndex >= len(rightData):
                    break
                if leftData[leftIndex] < rightData[rightIndex]:
                    dataList[index] = leftData[leftIndex]
                    leftIndex += 1
                else:
                    dataList[index] = rightData[rightIndex]
                    rightIndex += 1
            if leftIndex >= len(leftData):
                dataList[index:] = rightData[rightIndex:]
            else:
                dataList[index:] = leftData[leftIndex:]
    return dataList


if __name__ == "__main__":
    # Generate a random sample of 10 elements between -100 and 100
    inputList = random.sample(range(-10**15, 10**15), 10**7)
    # print("Input list: {}".format(inputList))
    # Sort in ascending order
    startTime = time.time()
    ascSort = mergeInsertionSort(inputList)
    print("Time taken: {}".format(time.time() - startTime))
    # print("Sorted list in ascending order: {}".format(ascSort))

    # # Sort in descending order
    # descSort = mergeInsertionSort(inputList, reverse=True)
    # print("Sorted list in descending order: {}".format(descSort))
