from typing import List

NUM_TO_CHAR = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def backtrack(digits, ans, cur_num):
    if not digits:
        return

    if len(cur_num) == len(digits):
        # 递归终点，当前的数字长度已经到底了
        ans.append("".join(cur_num))
        return

    digit = digits[len(cur_num)]
    chars = NUM_TO_CHAR[int(digit)]
    for ch in chars:
        cur_num.append(ch)
        backtrack(digits, ans, cur_num)
        cur_num.pop()


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        backtrack(digits, ans, [])
        return ans


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations(""))
