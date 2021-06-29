from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, ch in enumerate(s):
            ch_location = d.get(ch, [i, i])
            ch_location[1] = i
            d[ch] = ch_location

        location_list = sorted(list(d.values()))

        ans = []
        start = 0
        for i in range(len(location_list) - 1):
            if location_list[i + 1][0] < location_list[i][1]:
                # 相交
                location_list[i + 1][1] = max(location_list[i + 1][1], location_list[i][1])
            else:
                # 不相交
                ans.append(location_list[i][1] - start + 1)
                start = location_list[i + 1][0]
        ans.append(location_list[-1][1] - start + 1)
        return ans


if __name__ == '__main__':
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
    print(Solution().partitionLabels(""))
