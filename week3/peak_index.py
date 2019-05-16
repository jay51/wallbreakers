class Solution:
    # linear solution
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not(len(A) >= 3):
            return 0
            
        for ndx, el in enumerate(A):
            if ndx != len(A):
                if el > A[ndx - 1] and el > A[ndx + 1]:
                    return ndx
        
    # Iterative binary search 
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A) -1
        
        while right >= left:
            mid = left + (right - left) // 2
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid -1
            
        return left



    # Recursive binary search
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not(len(A) >= 3):
            return 0
        return self.b_search(A, 0, len(A)-1)
        
        
    def b_search(self, A, l, r):
        
        # if this is is false then 'l' will be a peak point
        if r >= l:
            # find the mid point 
            mid = l + (r -l) // 2
            # if the current mid point is less then the number to the right of  it then, we're still moving up
            if A[mid] < A[mid + 1]:
                return self.b_search(A, mid +1, r)
            else:
                return self.b_search(A, l, mid -1)
        else:
            return l
        
        
