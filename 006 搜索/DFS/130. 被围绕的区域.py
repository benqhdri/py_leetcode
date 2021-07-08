from typing import List

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(board, i, j, m, n, visited):
    queue = [[i, j]]
    visited[i][j] = True
    board[i][j] = ''
    while queue:
        cur = queue.pop()
        for d in DIRECTIONS:
            ne = [cur[0] + d[0], cur[1] + d[1]]
            if 0 <= ne[0] < m and 0 <= ne[1] < n \
                    and not visited[ne[0]][ne[1]] \
                    and board[ne[0]][ne[1]] == "O":
                # 没访问过，且是O
                visited[ne[0]][ne[1]] = True
                board[ne[0]][ne[1]] = ''
                queue.append(ne)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in (0, m - 1):
            for j in range(n):
                if not visited[i][j] and board[i][j] == "O":
                    bfs(board, i, j, m, n, visited)
        for j in (0, n - 1):
            for i in range(m):
                if not visited[i][j] and board[i][j] == "O":
                    bfs(board, i, j, m, n, visited)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif not board[i][j]:
                    board[i][j] = 'O'


if __name__ == '__main__':
    board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]
    print(Solution().solve(board))
    print(board)
