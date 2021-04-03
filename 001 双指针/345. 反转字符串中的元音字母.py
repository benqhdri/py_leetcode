VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


def swap(ls: list, low: int, high: int) -> list:
    ch = ls[low]
    ls[low] = ls[high]
    ls[high] = ch


class Solution:

    def reverseVowels(self, s: str) -> str:
        """
        以字符串作为输入，反转该字符串中的元音字母。
        """
        low = 0
        high = len(s) - 1
        ls = list(s)

        while low < high:
            while low < high and s[low] not in VOWELS:
                low += 1
            while low < high and s[high] not in VOWELS:
                high -= 1
            if low >= high:
                break
            if s[low] != s[high]:
                swap(ls, low, high)

            low += 1
            high -= 1
        return "".join(ls)


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))
