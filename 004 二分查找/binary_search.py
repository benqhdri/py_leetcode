from typing import List


def binary_search(nums: List, key: int) -> int:
    l, h = 0, len(nums) - 1
    while l <= h:
        m = l + (h - l) // 2
        if nums[m] == key:
            return m
        elif nums[m] > key:
            h = m - 1
        else:
            l = m + 1
    return -1
