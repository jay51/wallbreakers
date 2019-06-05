"""
Time : O(n)
Space: O(1)
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k > length:
            if k % length == 0: return
            else: self.switch(nums, k % length)
                
        else:
            self.switch(nums, k)
                
                
    def switch(self,nums, k):
        length = len(nums) - k
        for idx in range(len(nums)):
            if idx >= length:
                last = nums.pop()
                nums.insert(0, last)
                
