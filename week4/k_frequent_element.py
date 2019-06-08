"""
Time: O(nlog(k)) The complexity of Counter method is O(n). 
To build a heap and output list takes O(nlog(k)).
Hence the overall complexity of the algorithm is O(n + nlog(k)) = O(nlog(k))

Space: O(n)
"""
import heapq
import collections 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.Counter(nums)
        return heapq.nlargest(k, hashmap.keys(), key= lambda key: hashmap[key])
    
    """
        print(hashmap.keys())
        print(hashmap.values())
        largest = heapq.nlargest(k, hashmap.values())
        res = []
        for key in hashmap:
            if hashmap[key] in largest:
                res.append(key)
            
        return res
    """

