
class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(f"myPow({x}, {n})")
        if n == 0: return 1;
        
        if n < 0:
            n = -n;
            x = 1/x;
            
        if n % 2 == 0:
            y = self.myPow(x, n/2)
            return y * y
        else:
            res = x * self.myPow(x, n-1)
            return res
            
    def myPow(self, x: float, n: int) -> float:
        
        return x ** n
