from typing import List

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(grid, i, j, m, n):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
        return

    grid[i][j] = '0'
    for d in DIRECTIONS:
        dfs(grid, i + d[0], j + d[1], m, n)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j, m, n)
                    island_num += 1

        return island_num


if __name__ == '__main__':
    print(Solution().numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
