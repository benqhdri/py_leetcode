from typing import List


def find_left(nums, target):
    """返回小于target的最右边的数的坐标"""
    l, h = 0, len(nums) - 1
    while l <= h:
        m = l + (h - l) // 2
        if nums[m] >= target:
            h = m - 1
        else:
            l = m + 1

    return h


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = find_left(nums, target) + 1
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = find_left(nums, target + 1)

        return [left, right]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
    nums = []
    target = 8
    print(Solution().searchRange(nums, target))

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(Solution().searchRange(nums, target))

    nums = [1]
    target = 1
    print(Solution().searchRange(nums, target))

    nums = [2, 2]
    target = 3
    print(Solution().searchRange(nums, target))
