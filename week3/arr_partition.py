
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not len(nums): return 0
        sums = 0
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            sums += nums[i]
        return sums

