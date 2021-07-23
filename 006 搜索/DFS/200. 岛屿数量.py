from typing import List

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return

            grid[x][y] = '0'
            for d1, d2 in DIRECTIONS:
                nx, ny = x + d1, y + d2
                dfs(nx, ny)

        island_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    island_num += 1

        return island_num


if __name__ == '__main__':
    print(Solution().numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
