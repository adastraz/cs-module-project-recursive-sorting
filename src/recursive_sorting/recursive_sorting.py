    # TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    x = 0 
    y = 0
    merged_arr = []
    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr.append(arrA[x])
            x += 1
            # print(merged_arr)
        else:
            merged_arr.append(arrB[y])
            y += 1
            # print(merged_arr)
    merged_arr += arrA[x:]
    merged_arr += arrB[y:]
    # print(merged_arr)
    return merged_arr
    
# print(merge([1,2,3,4], [3,5,6,7]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr,sep=True):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        # print('left', left, 'right', right, 'mid', mid)
        return merge(left, right)
    return arr
# print(merge_sort([1,32,3,26,6,4,6,8]))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index-1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        m = (l + r) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
