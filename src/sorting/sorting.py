# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Initial values for variables that we use to keep
    # track of where we are in each array
    a = b = 0

    # Go through both copies until we run out of elements in one
    for i in range(elements):

        if a == len(arrA):
            merged_arr[i:] = arrB[b:]
            break
        if b == len(arrB):
            merged_arr[i:] = arrA[a:]
            break

        if arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


print(merge([4, 4, 5, 6, 9, 9, 9, 10], [3, 7, 9, 10]))


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        return merge(merge_sort(arr[len(arr) // 2:]), merge_sort(arr[:len(arr) // 2]))


print(merge_sort([8, 2, 4, 16, 54, 23, 42]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
# Your code here


# def merge_sort_in_place(arr, l, r):
# Your code here
