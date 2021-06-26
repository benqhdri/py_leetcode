from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []

        # 身高升序，位置降序
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        for p in people:
            if len(ans) <= p[1]:
                ans.append(p)
            else:
                ans.insert(p[1], p)

        return ans


"""
if __name__ == '__main__':
    print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(Solution().reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
"""
