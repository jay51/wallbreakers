"""
Time : O(n^2)
Space: O(n)
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for start in range(len(s)):
            longest = max(longest, self.help(s, start))
        
        return longest
            
        
    def help(self, string,  start):
        seen = ""
        for idx in range(start, len(string)):
            if string[idx] not in seen:
                seen += string[idx]
            else:
                return idx - start
        return len(string) - start
                
    """
    Time : O(n)
    Space: O(1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = {}
        start = 0

        for idx, char in enumerate(s):
            if char in seen:
                # set the start to idx of char + 1
                #start = max(start, seen[char] +1 )
                if start < seen[char] +1:
                    start = seen[char] +1

            seen[char] = idx
            # get length of substring from start to current char
            #longest = max(longest, idx - start + 1)
            if idx - start + 1 > longest:
                longest = idx - start +1

        return longest

