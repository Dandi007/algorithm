import random
from typing import List


def bubble_sort(arr: List[int]):
    n = len(arr)
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr


n = 50

arr = [random.randint(0, 50) for i in range(n)]
bubble_sort(arr)

print(arr)
