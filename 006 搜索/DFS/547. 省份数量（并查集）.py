from typing import List


class UnionFind:
    def __init__(self, count):
        self.father = {}
        self.count = count

    def find(self, x):
        self.father.setdefault(x, x)
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy: return
        self.father[fx] = fy
        self.count -= 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.count


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(Solution().findCircleNum(isConnected))
