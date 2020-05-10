import random
from typing import List


def merge_sort(arr, l, r):
    """

    一开始传的是python的子序列 arr[:],但是总是有莫名其妙的问题
    后面改成传整个数组 && 对应的下标范围,就ok了
    但是最好还是注意一下,了解一下为啥有这个问题
    """
    n = r - l
    if n == 1 or n == 2:
        if n == 2:
            if arr[l] > arr[l+1]:
                arr[l] = arr[l] ^ arr[l+1]
                arr[l+1] = arr[l] ^ arr[l+1]
                arr[l] = arr[l] ^ arr[l+1]
        return
    mid = (l+r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid, r)
    # merge arr
    temp = [None] * n
    l_index = l
    r_index = mid
    i = 0
    while l_index < mid and r_index < r:
        if arr[l_index] <= arr[r_index]:
            temp[i] = arr[l_index]
            l_index += 1
        else:
            temp[i] = arr[r_index]
            r_index += 1
        i += 1
    while l_index < mid:
        temp[i] = arr[l_index]
        l_index += 1
        i += 1
    while r_index < r:
        temp[i] = arr[r_index]
        r_index += 1
        i += 1
    for i in range(n):
        arr[l+i] = temp[i]


n = 30

arr = [random.randint(0, n) for i in range(n)]
merge_sort(arr, 0, n)
print(arr)
