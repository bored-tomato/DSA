def insertionSort(input_list):
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        keyPosition = findKeyPos(input_list, key, j)
        input_list[keyPosition] = key

def insertionSortRecursive(input_list, n):
    if n == 0: return input_list[0]
    insertionSortRecursive(input_list, n - 1)

    key = input_list[n]
    j = n - 1
    keyPosition = findKeyPos(input_list, key, j)
    input_list[keyPosition] = key

def findKeyPos(input_list, key, prevIndex):
    while(prevIndex >= 0 and key < input_list[prevIndex]):
        input_list[prevIndex + 1] = input_list[prevIndex]
        prevIndex -= 1
    return prevIndex + 1