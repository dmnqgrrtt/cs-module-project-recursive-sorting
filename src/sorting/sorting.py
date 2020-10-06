# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    aIndex = 0
    bIndex = 0
    

    while aIndex < len(arrA) and bIndex < len(arrB):
        if arrA[aIndex] < arrB[bIndex]:
            merged_arr.append(arrA[aIndex])
            aIndex += 1
            
        else:
            merged_arr.append(arrB[bIndex])
            bIndex += 1
            

    if aIndex == len(arrA):
        while bIndex < len(arrB):
            merged_arr.append(arrB[bIndex])
            
            bIndex += 1
    else:
         while aIndex < len(arrA):
            merged_arr.append(arrA[aIndex])
            
            aIndex += 1



    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        middle = len(arr)  // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

merge([1,2], [1,2])