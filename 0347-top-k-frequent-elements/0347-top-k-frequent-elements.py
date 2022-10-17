class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1
        counts = collections.Counter(nums)
        return sorted(counts.keys(), key = lambda x: counts[x], reverse=True)[:k]