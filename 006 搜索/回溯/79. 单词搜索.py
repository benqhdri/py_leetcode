from typing import List

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def backtrack(x, y, cur):
            if len(cur) == len(word):
                return True

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    # 越界
                    continue
                if vis[nx][ny]:
                    # 访问过
                    continue
                if board[nx][ny] != word[len(cur)]:
                    continue

                vis[nx][ny] = True
                cur.append(board[nx][ny])
                backtrack(nx, ny, cur)
                cur.pop()
                vis[nx][ny] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis[i][j] = True
                    if backtrack(i, j, [board[i][j]]):
                        return True
                    vis[i][j] = False

        return False

