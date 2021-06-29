class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        start = 0
        for ch in s:
            start = t.find(ch, start) + 1
            if start == 0:
                return False
        return True


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))

    s = "axc";
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))

    s = "aaaaaa"
    t = "bbaaaa"
    print(Solution().isSubsequence(s, t))
