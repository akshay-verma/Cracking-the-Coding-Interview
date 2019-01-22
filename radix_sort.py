
def _sort(dataList, divide):
    counter = [None] * (max(dataList) + 1)
    for index, data in enumerate(dataList):
        data = data // divide
        if counter[data]:
            counter[data].append(index)
        else:
            counter[data] = [index]
    dataList = []
    for val in counter:
        dataList.append(val)
    return dataList


def getDataListFromIndex(dataList, indexList):
    data = []
    for index in indexList:
        if index:
            for val in index:
                data.append(dataList[val])
    return data


def countingSort(dataList):
    indexList = _sort(dataList, 1)
    return getDataListFromIndex(dataList, indexList)


def radixSort(dataList):
    maxNum = max(dataList)
    count = 0
    while maxNum > 0:
        indexList = _sort(dataList, 10**count)
        dataList = getDataListFromIndex(dataList, indexList)
        maxNum = maxNum // 10
        count += 1
    return dataList


if __name__ == "__main__":
    dataList = [17, 998, 0, 0, 1, 2, 4, 5, 2, 7, 8, 9, 1, 0]
    print(radixSort(dataList))
    print(countingSort(dataList))
