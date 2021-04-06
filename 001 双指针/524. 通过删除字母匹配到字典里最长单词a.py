from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            index = 0
            for ch in word:
                index = s.find(ch, index) + 1
                if not index:
                    break
            else:
                return word
        return ''
