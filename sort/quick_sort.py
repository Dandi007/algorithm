import random
from typing import List


def partation(arr: List[int], l: int, r: int):
    if r - l + 1 <= 1:
        return
    piviot = arr[(l + r) >> 1]

    # WHY need this switch?
    arr[r], arr[(l + r) >> 1] = piviot, arr[r]

    index = l
    for i in range(l, r):
        if arr[i] <= piviot:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1

    # WHY switch back here?
    arr[r], arr[index] = arr[index], arr[r]
    
    return index


def quick_sort(arr: List[int], l: int, r: int):
    k = partation(arr, l, r)
    partation(arr, l, k)
    partation(arr, k + 1, r)


n = 10
random.seed(0)
arr = [random.randint(0, n) for i in range(n)]
quick_sort(arr, 0, n-1)
print(arr)
