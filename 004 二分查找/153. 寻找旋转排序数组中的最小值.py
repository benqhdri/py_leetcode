from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            if nums[m] <= nums[h]:
                h = m
            else:
                l = m + 1

        return nums[h]


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(Solution().findMin(nums))
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(Solution().findMin(nums))
    nums = [11, 13, 15, 17]
    print(Solution().findMin(nums))
    nums = [5, 1, 2, 3, 4]
    print(Solution().findMin(nums))
