
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            if "0" in str(i): continue
            
            is_divisble = True
            for j in str(i):
                if i % int(j) != 0:
                    is_divisble = False
                    
            if is_divisble: result.append(i)
                
        return result
            
