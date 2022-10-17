class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1
        # counts = collections.Counter(nums)
        # return sorted(counts.keys(), key = lambda x: counts[x], reverse=True)[:k]
        
        # Method 2 (Clever Bucket Sort)
        countdict = collections.Counter(nums)
        freq = [[] for i in range(0,len(nums)+1)]
        
        for key,value in countdict.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            res.extend(freq[i])
            #print("It", i, freq[i], res, len(res), k)
            if len(res) >= k:
                #print("Len", len(res))
                return res[:k]
            
        
        