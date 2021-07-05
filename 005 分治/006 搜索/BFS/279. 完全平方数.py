import collections
import math


class Solution:
    def numSquares(self, n: int) -> int:
        square_set = set([i * i for i in range(1, int(math.sqrt(n)) + 1) if i * i <= n])

        min_num = 0
        queue = collections.deque()
        queue.append(n)

        while queue:
            min_num += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                for s in square_set:
                    ne = cur - s
                    if ne > 0:
                        queue.append(ne)
                    elif ne == 0:
                        return min_num

        return -1


"""
if __name__ == '__main__':
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))
    print(Solution().numSquares(1))
"""
