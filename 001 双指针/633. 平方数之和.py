from math import sqrt
from math import floor


class Solution:
    """
    给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
    """

    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = floor(sqrt(c))

        while low <= high:
            if c - low * low > high * high:
                low += 1
            elif c - low * low < high * high:
                high -= 1
            else:
                return True
        return False
