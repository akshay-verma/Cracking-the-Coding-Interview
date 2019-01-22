import random


def findMin(dataList):
    minNum = dataList[0]
    minIndex = 0
    for index in range(0, len(dataList)):
        if dataList[index] < minNum:
            minNum, minIndex = dataList[index], index
    return minNum, minIndex


def findMax(dataList):
    maxNum = dataList[0]
    maxIndex = 0
    for index in range(0, len(dataList)):
        if dataList[index] > maxNum:
            maxNum, maxIndex = dataList[index], index
    return maxNum, maxIndex


def selectionSort(dataList, reverse=False):
    """
    Sorts the list of element using selection sort in ascending order(default).
    In order to sort the elements in descending order,
    use the parameter reverse=True.

    Args:
        reverse(bool): Default=false. If set to True,
                       sort in descending order otherwise ascending.

    Returns:
        list: Sorted list of elements

    Raises:
        None
    """
    for index in range(0, len(dataList) - 1):
        if reverse:
            resNum, resIndex = findMax(dataList[index:])
        else:
            resNum, resIndex = findMin(dataList[index:])
        resIndex += index
        temp = dataList[index]
        dataList[index] = resNum
        dataList[resIndex] = temp
    return dataList


if __name__ == "__main__":
    # Generate a random sample of 10 elements between -100 and 100
    inputList = random.sample(range(-100, 100), 10)

    # Sort in ascending order
    ascSort = selectionSort(inputList)
    print("Sorted list in ascending order: {}".format(ascSort))

    # Sort in descending order
    descSort = selectionSort(inputList, reverse=True)
    print("Sorted list in descending order: {}".format(descSort))
