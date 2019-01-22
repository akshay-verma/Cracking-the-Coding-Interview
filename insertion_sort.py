import random


def insertionSort(dataList, reverse=False):
    """
    Sorts the list of element using insertion sort in ascending order(default).
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

    def compare(num1, num2, reverse):
        if reverse:
            return num1 > num2
        return num1 < num2

    for index in range(1, len(dataList)):
        num = dataList[index]
        for innerIndex in range(0, index):
            temp = dataList[innerIndex]
            if compare(num, temp, reverse):
                dataList[index] = temp
                dataList[innerIndex] = num
                num = temp
    return dataList


if __name__ == "__main__":
    # Generate a random sample of 10 elements between -100 and 100
    inputList = random.sample(range(-100, 100), 10)

    # Sort in ascending order
    ascSort = insertionSort(inputList)
    print("Sorted list in ascending order: {}".format(ascSort))

    # Sort in descending order
    descSort = insertionSort(inputList, reverse=True)
    print("Sorted list in descending order: {}".format(descSort))
