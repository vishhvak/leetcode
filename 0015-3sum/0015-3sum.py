class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            while start < end:
                threesum = a + nums[start] + nums[end]
                if threesum > 0:
                    end = end - 1
                elif threesum < 0:
                    start = start + 1
                elif threesum == 0:
                    res.append([a, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return res
        