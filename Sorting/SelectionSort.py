def selectionSort(input_list):
    for i in range(len(input_list)-1):
        min_index = i
        for j in range(i+1, len(input_list)):
            if(input_list[j] < input_list[min_index]):
                min_index = j
        swap(input_list, i, min_index)
        
def swap(input_list, index_1, index_2):
    input_list[index_1], input_list[index_2] = input_list[index_2], input_list[index_1]