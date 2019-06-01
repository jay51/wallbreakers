"""
Time : O(2n) or O(n+n)
Space: O(n)
"""
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        for s in ops:
            
            # if s == + add top of stack and second top of stack and push as new top of stack
            if s == "+":
                top = stack.pop()
                new_top = top + stack[-1]
                stack.append(top)
                stack.append(new_top)
            
            # pop the top of stack
            elif s == "C":
                stack.pop()
            
            # multiplay the top of stack by 2 and push as new top of stack
            elif s == "D":
                stack.append(2 * stack[-1])
            
            else:
                stack.append(int(s))
             

        return sum(stack)
            
