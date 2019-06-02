"""
Time : O(n)
Space: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        
        stack = []
        for char in s:
            if char == ")":
                if not stack or stack.pop() != "(": # check if stack is empty before pop
                    return False
                    
            elif char == "}":
                if not stack or stack.pop() != "{": # check if stack is empty before pop
                    return False
                
            elif char == "]":
                if not stack or stack.pop() != "[": # check if stack is empty before pop
                    return False
                
            else:
                stack.append(char)
                
        if stack:
            return False
                
        return True
    

