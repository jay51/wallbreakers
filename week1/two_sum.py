
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            for i2, val2 in enumerate(nums[i+1:]):
                if val + val2 == target:
                    return [i, i2 + i +1]
            
        
