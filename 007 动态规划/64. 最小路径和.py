import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [sys.maxsize for _ in range(len(grid[0]) + 1)]
        dp[1] = 0

        for line in grid:
            for i, cost in enumerate(line):
                dp[i + 1] = min(dp[i], dp[i + 1]) + cost
        return dp[-1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    grid = [[1, 2, 3], [4, 5, 6]]
    grid = [[1, 2, 3]]
    print(Solution().minPathSum(grid))
