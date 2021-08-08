class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        pre2, pre1, ans = 1, 2, 3
        for _ in range(n - 2):
            ans = pre1 + pre2
            pre2 = pre1
            pre1 = ans
        return ans


if __name__ == '__main__':
    print(Solution().climbStairs(10))
