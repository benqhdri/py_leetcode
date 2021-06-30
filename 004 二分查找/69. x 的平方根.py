class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l, h = 1, x
        while l <= h:
            m = l + (h - l) // 2
            sqrt = x // m
            if sqrt > m:
                l = m + 1
            elif sqrt < m:
                h = m - 1
            else:
                return m
        return h


if __name__ == '__main__':
    print(Solution().mySqrt(9))
