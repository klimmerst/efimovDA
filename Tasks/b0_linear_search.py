"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

test = [10, 2, 0, 0]

def min_search(arr: Sequence) -> int:

    if not arr:
        return - 1

    min = 0
    index = 0

    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
        print(i)


    return index

print(min_search(test))
