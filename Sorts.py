from random import randrange

#function that swaps adjacent values in a list
def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

#merge function to be used in merge sort
def merge(left, right):
    result = []

    #loop through sub-lists, add smaller element to result and remove from sub-list
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    #add remaining elements to result list
    if left:
        result += left
    if right:
        result += right

    return result

#simple bubble sort function
def bubble_sort(arr):
    for j in arr:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                
def merge_sort(arr):
    if (len(arr)) <= 1:
        return arr
    
    #create sub-lists
    middle_index = len(arr) // 2
    left_split = arr[:middle_index]
    right_split = arr[middle_index:]

    #sort the sub-lists
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

def quick_sort(arr, start, end):
    if start >= end:
        return arr
    
    #choose a random element to compare elements to
    pivot_index = randrange(start, end + 1)
    pivot_element = arr[pivot_index]

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    less_than_pointer = start

    for i in range(start, end):
        if arr[i] < pivot_element:
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1
    
    arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]

    quick_sort(arr, start, less_than_pointer - 1)
    quick_sort(arr, less_than_pointer + 1, end)
