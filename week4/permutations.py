class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        prem = []
        self.helper(nums, [], prem)
        return prem
    
    def helper(self, nums, selected, prem):
        if not len(nums):
            prem.append(list(selected))
            return
        
        for idx, el in enumerate(nums):
            selected.append(el)
            rest = nums[:idx] + nums[idx + 1: ]
            self.helper(rest, selected, prem)
            selected.pop()
