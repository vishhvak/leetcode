class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        antiele = {}
        for i in range(0, len(nums)):
            if target-nums[i] in antiele:
                return [i, antiele[target-nums[i]]]
            else:
                antiele[nums[i]] = i
        