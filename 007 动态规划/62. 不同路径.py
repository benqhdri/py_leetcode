class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        dp[0] = 0

        for _ in range(m - 1):
            for i in range(n):
                dp[i + 1] += dp[i]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 3))
