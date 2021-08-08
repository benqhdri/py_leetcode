from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp数组在前面多补3个0
        dp = [0 for _ in range(len(nums) + 3)]
        for i, num in enumerate(nums):
            dp[i + 3] = max(dp[i + 2], dp[i + 1] + num, dp[i] + num)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().rob([2, 1, 1, 2]))
    print(Solution().rob([2, 7, 9, 3, 1]))
