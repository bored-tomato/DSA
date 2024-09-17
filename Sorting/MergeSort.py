def mergeSort(input_list, start, end):
    if(start == end): return input_list[start]
    mid = int((end-start)/2 + start)
    print(f"Start: {start}\tMid: {mid}\tEnd: {end}")
    mergeSort(input_list, start,mid)
    mergeSort(input_list, mid+1, end)
    combine(input_list, start, mid, end)

def combine(input_list, start, mid, end):
    leftArr = input_list[start:mid+1]
    rightArr = input_list[mid+1:end+1]

    i,j,k = 0,0,start

    while(i < len(leftArr) and j < len(rightArr)):
        if(leftArr[i] <= rightArr[j]):
            input_list[k] = leftArr[i]
            i+=1
            k+=1
        else:
            input_list[k] = rightArr[j]
            j+=1
            k+=1
    while(i < len(leftArr)):
        input_list[k] = leftArr[i]
        i+=1
        k+=1
    
    while(j < len(rightArr)):
        input_list[k] = rightArr[j]
        j+=1
        k+=1