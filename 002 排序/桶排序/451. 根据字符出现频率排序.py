from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(i[0] * i[1] for i in Counter(s).most_common(len(s)))
