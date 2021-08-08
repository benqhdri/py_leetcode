from typing import List


def rob_without_circle(nums: List[int]) -> int:
    # dp数组在前面多补3个0
    dp = [0 for _ in range(len(nums) + 3)]
    for i, num in enumerate(nums):
        dp[i + 3] = max(dp[i + 2], dp[i + 1] + num, dp[i] + num)
    return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        """环形抢劫，分两种情况，抢第一家的和不抢第一家
            1、抢第一家，则最后一家可以排除，其他都按线性抢劫
            2、不抢第一家，则按去掉第一家的方式来计算
            两者取大者，即为最终答案

        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]

        return max(rob_without_circle(nums[1:]), rob_without_circle(nums[:-1]))


if __name__ == '__main__':
    print(Solution().rob(nums=[2, 3, 2]))
    print(Solution().rob(nums=[1, 2, 3, 1]))
