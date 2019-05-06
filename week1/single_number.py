
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        first = nums[0]
        for i in nums[1:]:
            first = first ^ i

        return first
