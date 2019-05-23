"""
Time : O(n)
Space: O(1)
"""
class Solution(object):
    def reverse(self, x):
        rev= 0
        sign = False
        if x < 0:
            x = abs(x)
            sign = True

        # Example: x = 21
        # rev= 0
        # x = 21
        ###########
        # rev= 1
        # x = 2
        ###########
        # rev= 12
        # x = 0
            
        while( x != 0):
            # take the last char and add it to rev  => 0 + 21 % 10 = 1
            rev= rev*10 + x % 10
            # take the last char out of x
            x = x/10
            if rev > 2147483647  or rev < -2147483648 :
                return 0
        
        if sign:
            return int("-" + str(rev))
            
        return rev
