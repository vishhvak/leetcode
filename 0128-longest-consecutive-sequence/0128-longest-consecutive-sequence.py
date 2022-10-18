class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Define set of numbers 
        numset = set(nums)
        max_length = 0
        
        for n in nums:
            # Check for left neighbor in the set 
            if n-1 not in numset:
                # If no left neighbor, it is the start of a sequence
                length = 0
                # Check for consecutive elements and build the sequence
                while (n+length) in numset:
                    length += 1
                # Compare the length you got with the longest length
                max_length = max(max_length, length)
        # Return longest length recorded
        return max_length
                
        