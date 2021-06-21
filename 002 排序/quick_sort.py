from typing import List


def _partition(arr, l, h):
    i = l - 1
    pivot = arr[h]

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def _quick_sort(arr, l, h):
    if l < h:
        pi = _partition(arr, l, h)
        _quick_sort(arr, l, pi - 1)
        _quick_sort(arr, pi + 1, h)


def quick_sort(arr, l=0, h=None):
    if not h:
        h = len(arr) - 1

    _quick_sort(arr, l, h)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        quick_sort(nums)
        return nums[-k]
