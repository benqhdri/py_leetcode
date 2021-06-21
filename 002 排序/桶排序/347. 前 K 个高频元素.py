from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # 计数工具
        return sorted(count, key=count.get, reverse=True)[:k]  # 根据频率排序取前k个
