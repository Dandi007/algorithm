from typing import List


def select_sort(arr: List[int]):
    """选择排序,副作用为改变arr内部元素的顺序,返回升序的arr,时间复杂度n^2
    """
    n = len(arr)
    for i in range(n):
        min_index = None
        min_num = arr[i]
        for j in range(i+1, n):
            if arr[j] < min_num:
                min_index = j
                # 一开始忘记这里,导致选择排序都可以写错
                min_num = arr[j]
        if min_index is not None:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
            """
            可以用位运算来避免额外的空间开销
            a = a ^ b
            b = a ^ b
            a = a ^ b
            (^为python中的xor)
            """
    return arr

import random

n = 5000
arr = []
for i in range(n):
    arr.append(random.randint(0,1000))

true_arr = sorted(arr)
my_arr = select_sort(arr)
for i in range(n):
    if true_arr[i] != my_arr[i]:
        print('false')
        print(true_arr[i],my_arr[i],i)
        break
