from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, h = 0, len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            elif (nums[m] == nums[m - 1] and m % 2 == 1) \
                    or (nums[m] == nums[m + 1] and m % 2 == 0):
                l = m + 1
            else:
                h = m - 1

        return nums[l]


if __name__ == '__main__':
    print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
    print(Solution().singleNonDuplicate([3, 3, 7, 7, 10]))
    print(Solution().singleNonDuplicate([3, 3, 10]))
    print(Solution().singleNonDuplicate([2, 3, 3]))
