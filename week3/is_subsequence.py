class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_s = len(s)
        if length_s == 0:
            return True
        
        if length_s > len(t):
            return False
        
        sub_string = ""
        index = 0
        for char in t:
            if index == length_s:
                return True
            if char == s[index]:
                sub_string += char
                index +=1
        
        return sub_string == s
            
            
        
