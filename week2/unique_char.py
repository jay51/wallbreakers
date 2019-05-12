
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for idx, char in enumerate(s):
            string = s[:idx] + s[idx + 1:]
            if char not in string:
                return idx
        return -1
