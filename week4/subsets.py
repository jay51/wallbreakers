"""
Time : O(2^n) as total 2^n possible subsets can be there for n items.
Space: O(n+n) = O(n) is the maximum depth of recursion tree + 'num' list space
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        self.helper(0, nums, [], subset)
        return subset
        
        
    def helper(self, index, nums, current_set, subset):
        subset.append(list(current_set))
        #print(current_set)
        
        for idx in range(index, len(nums)):
            current_set.append(nums[idx])
            self.helper(idx + 1, nums, current_set, subset)
            poped = current_set.pop()
            #print("poping", poped)
