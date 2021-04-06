from typing import List


def is_substring(s: str, sub_string: str) -> bool:
    i = 0
    j = 0
    while i < len(s) and j < len(sub_string):
        while i < len(s) and s[i] != sub_string[j]:
            i += 1
        if i != len(s):
            i += 1
            j += 1
    return j == len(sub_string)


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ''
        for word in dictionary:
            if is_substring(s, word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        return ans

# if __name__ == '__main__':
#     print(Solution().findLongestWord("abpcplea",
#                                      ["ale", "apple", "monkey", "plea", "abpcplaaa", "abpcllllll",
#                                       "abccclllpppeeaaaa"]))
