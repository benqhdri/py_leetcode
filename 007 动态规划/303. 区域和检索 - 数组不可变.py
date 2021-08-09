from typing import List


def get_sums(nums):
    sums = nums.copy()
    for i in range(1, len(sums)):
        sums[i] += sums[i - 1]

    return sums


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = get_sums(nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] if left == 0 else self.sums[right] - self.sums[left - 1]
