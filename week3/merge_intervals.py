
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not len(intervals): return []
        
        intervals.sort(key= lambda x: x[0])
        result = []
        for start, end in intervals:
            # if no previous el or start of current el is larger then end of previous el
            if not len(result) or start > result[-1][1]: 
                result.append([start, end])
            else:
                # end should merge to the largest end of both el
                result[-1][1] = max(result[-1][1], end)
                
        return result
            
