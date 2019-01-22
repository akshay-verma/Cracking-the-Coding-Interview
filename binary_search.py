import random


def binarySearch(dataList, num):
    index = len(dataList) // 2
    prevIndex = None
    while(index != 0 or index != len(dataList) - 1):
        # print("Prev Index: {}".format(prevIndex))
        # print("Index: {}".format(index))
        if dataList[index] == num:
            return index
        elif dataList[index] > num:
            prevIndex = index
            index = index // 2
        else:
            if not prevIndex:
                prevIndex = len(dataList)
            index = (index + prevIndex) // 2
    return None


if __name__ == "__main__":
    dataList = sorted(random.sample(range(-100, 100), 10))
    for index in range(0, 10):
        num = dataList[index]
        print("Input list: {}".format(dataList))
        print("Search for number: {}\tIndex: {}".format(num, index))
        result = binarySearch(dataList, num)
        print(result)
