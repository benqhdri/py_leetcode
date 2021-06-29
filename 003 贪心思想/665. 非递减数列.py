from typing import List


def is_not_decrease(l):
    """判断当前数组是否非递减"""
    return l == sorted(l)


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # 非递减了
                l1 = nums.copy()
                l1.pop(i)
                l2 = nums.copy()
                l2.pop(i + 1)
                return is_not_decrease(l1) or is_not_decrease(l2)
        return True


if __name__ == '__main__':
    nums = [4, 2, 3]
    print(Solution().checkPossibility(nums))

    nums = [4, 2, 1]
    print(Solution().checkPossibility(nums))
