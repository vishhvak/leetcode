class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0]*len(nums)
        prefix = 1
        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        #print(res)
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res