def binarySearch(input_list, target):
    start, end = 0, len(input_list) - 1

    while(start <= end):
        mid = int((end-start)/2 + start)
        if(input_list[mid] == target): return mid
        elif(input_list[mid] < target): start = mid + 1
        else: end = mid - 1

    return -1

def binarySearchRecursive(input_list, start, end, target):
    if(start <= end):
        mid = int((end-start)/2 + start)
        if(input_list[mid] == target): return mid
        elif(input_list[mid] < target): return binarySearchRecursive(input_list, mid + 1, end, target)
        else: return binarySearchRecursive(input_list, start, mid - 1, target)
        
    else: return -1