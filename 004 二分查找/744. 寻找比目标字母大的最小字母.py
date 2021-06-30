from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        l, h = 0, len(letters) - 1
        while l < h:
            m = l + (h - l) // 2
            if letters[m] > target:
                h = m
            else:
                l = m + 1
        return letters[l]

if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "a"
    print(Solution().nextGreatestLetter(letters, target))
    target = "c"
    print(Solution().nextGreatestLetter(letters, target))
    target = "d"
    print(Solution().nextGreatestLetter(letters, target))
    target = "g"
    print(Solution().nextGreatestLetter(letters, target))
    target = "j"
    print(Solution().nextGreatestLetter(letters, target))
    target = "k"
    print(Solution().nextGreatestLetter(letters, target))
