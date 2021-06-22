from typing import List


def swap(nums, l, r):
    nums[l], nums[r] = nums[r], nums[l]


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, r = -1, 0, len(nums)
        # 不用管0，直接遍历即可
        while i < r:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                l += 1
                swap(nums, i, l)
                i += 1
            elif nums[i] == 2:
                r -= 1
                swap(nums, i, r)
            else:
                raise Exception(f"not support value: {nums[i]}")
