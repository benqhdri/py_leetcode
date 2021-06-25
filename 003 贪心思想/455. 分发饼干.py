from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            # 小孩分完了，或是饼干没了
            if g[i] <= s[j]:
                # 够分
                i += 1
            j += 1
        return i
