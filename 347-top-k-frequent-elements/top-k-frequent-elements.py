class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [elem for elem, _ in Counter(nums).most_common(k)]
        