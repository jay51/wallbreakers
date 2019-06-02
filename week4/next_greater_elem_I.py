"""
Time : O(n)
Space: O(n)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        maps = {}
        stack = []
        if not len(nums1): return stack
        
        # get the next greater element for all elements in nums2
        for num in nums2:
            # if next elem > then elem on top of stack then recored and pop and continue down the stack  
            while stack and num > stack[-1]:
                maps[stack.pop()] = num
            
            stack.append(num)
        
        result = []
        for key in nums1:
            # everything left in stack has no next greater element 
            if key in stack:
                result.append(-1)
                
            else:
                result.append(maps[key])
            
        return result
            
