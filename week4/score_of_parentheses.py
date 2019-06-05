"""
Time : O(n)
Space: O(n)
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        #() () () ( () )
        stack = []
        cur = 0
        
        for idx, char in enumerate(S):
            # push to stack and reset cur layer
            if char == "(":
                stack.append(cur)
                cur = 0
            else:
                # it's ), so pop prev socer off stack + cur * 2 if there's inner layers or 1
                cur = max(cur * 2, 1) + stack.pop() 
    
        return cur

