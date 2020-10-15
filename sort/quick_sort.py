import random
from typing import List


def partation(arr: List[int], l: int, r: int):
    piviot = arr[(l + r) >> 1]

    # WHY need this switch?
    # 如果piviot恰好是最大的,那么不做switch的话,这次partation将不会对整个序列做任何调整
    # 通过这次强行移动,确保了返回的index上一定是这次partation最大的元素,就可以在外层的sort
    # 来跳过这个元素,保证每一次sort都会起码在待排序序列中去除一个元素
    arr[r], arr[(l + r) >> 1] = piviot, arr[r]

    index = l  # index to save item less or equal than pivot
    for i in range(l, r):
        if arr[i] <= piviot:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1

    # 把pivot放在<=pivot的序列的后方,并且把其index返回,用于从待排序序列中去除pivot
    arr[r], arr[index] = (
        arr[index],
        arr[r],
    )
    return index


def quick_sort(arr: List[int], l: int, r: int):
    if r - l <= 1:
        return
    k = partation(arr, l, r)
    # 在待排序序列中去除起码一个元素
    # 以及递归调用sort而非partition
    quick_sort(arr, l, k - 1)
    quick_sort(arr, k + 1, r)


n = 10
random.seed(0)
arr = [random.randint(0, n) for i in range(n)]
quick_sort(arr, 0, n - 1)
print(arr)
