import collections
from typing import List

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(grid, i, j, m, n):
    queue = collections.deque()
    queue.append([i, j])
    grid[i][j] = 0
    area = 0
    while queue:
        area += len(queue)
        for _ in range(len(queue)):
            cur = queue.popleft()
            for d in DIRECTIONS:
                ne = [cur[0] + d[0], cur[1] + d[1]]
                if 0 <= ne[0] < m and 0 <= ne[1] < n and grid[ne[0]][ne[1]] == 1:
                    queue.append(ne)
                    grid[ne[0]][ne[1]] = 0
    return area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = bfs(grid, i, j, m, n)
                    max_area = max(max_area, cur_area)

        return max_area


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland(
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
