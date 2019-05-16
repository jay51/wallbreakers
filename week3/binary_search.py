class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if not len(nums):
            return -1
        
        return self.b_search( nums, 0, len(nums) -1, target)
        

        
    def b_search(self, nums, left, right, target):
        
        if right >= left:
            
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                # move right to bigger numbers
                print("search right half")
                return self.b_search(nums, mid + 1, right , target)

            else:
                # move left to smaller numbers
                print("search left half")
                return self.b_search(nums, left, mid - 1, target)
        else:
            return -1
