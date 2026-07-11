class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:          
                length = 1
                curr = num + 1
                while curr in s:
                    length += 1
                    curr += 1
                longest = max(longest, length)
        return longest
        