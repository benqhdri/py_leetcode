import collections
from typing import List


def bfs(isConnected, i, n):
    queue = collections.deque()
    queue.append(i)
    isConnected[i][i] = 0
    while queue:
        cur = queue.popleft()
        for ne in range(n):
            if isConnected[cur][ne]:
                isConnected[ne][ne] = isConnected[cur][ne] = isConnected[ne][cur] = 0
                queue.append(ne)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        prov_num = 0
        for i in range(n):
            if isConnected[i][i] == 1:
                bfs(isConnected, i, n)
                prov_num += 1
        return prov_num
