def isPalindrome(s: str) -> bool:
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return False
    return True


class Solution:
    """
    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

    """

    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return isPalindrome(s[low + 1:high + 1]) or isPalindrome(s[low:high])
        return True
