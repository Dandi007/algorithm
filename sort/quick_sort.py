import random
from typing import List


def quick_sort(arr: List[int], l: int, r: int):
    """
    Parameters:

    arr List[int]: array to sort

    l int: [l,r) lb of arr

    r int: [l,r) rb of arr 
    """
    n = r - l
    if n <= 1:
        return

    mid = (l+r) // 2
    anchor = arr[mid]
    arr[mid], arr[r-1] = arr[r-1], arr[mid]
    index = l
    for i in range(l, r-1):
        if arr[i] <= anchor:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    arr[r-1], arr[index] = arr[index], arr[r-1]
    # 重点:skip anchor本身在的那一个元素
    quick_sort(arr, l, index)
    quick_sort(arr, index+1, r)


n = 10

arr = [random.randint(0, n) for i in range(n)]
quick_sort(arr, 0, n)
print(arr)
