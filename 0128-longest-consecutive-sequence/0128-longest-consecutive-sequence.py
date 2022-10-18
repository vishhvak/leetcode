class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = 0
        
        for n in nums:
            if n-1 not in numset:
                length = 0
                while (n+length) in numset:
                    length += 1
                max_length = max(max_length, length)
        return max_length
                
        