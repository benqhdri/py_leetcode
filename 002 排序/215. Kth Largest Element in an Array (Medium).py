import heapq
from typing import List

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """堆排序"""
        heapq.heapify(nums)
        nsmallest_nums = heapq.nsmallest(len(nums) - k + 1, nums)
        return nsmallest_nums[-1]
