from typing import List


def backtrack(s, ans, cur):
    if not s or len(cur) == 4:
        # 如果字符串用光了，或者cur的数字满了
        if not s and len(cur) == 4:
            # 要刚好s用完，且cur正好是4，才是一个解
            ans.append(".".join(cur))
        return

    for i in range(1, min(4, len(s) + 1)):
        num_str = s[:i]

        if num_str[0] == '0' and len(num_str) > 1:
            # 首位是0，且位数大于1
            continue

        if int(num_str) > 255:
            continue

        cur.append(num_str)
        backtrack(s[i:], ans, cur)
        cur.pop()


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        backtrack(s, ans, [])
        return ans


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("0000"))
