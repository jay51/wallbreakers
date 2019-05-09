
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        short = nums1
        large = nums2
        if len(short) > len(large):
            large = nums1
            short = nums2
            
        output = []
        for i in short:
            if i in large and i not in output:
                output.append(i)
            
        return output
            
