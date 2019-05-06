
class Solution:
    def binaryGap(self, N: int) -> int:
        index = [i for i, v in enumerate(bin(N)) if v == '1']
        result = 0
        length = len(index) -1
        
        for i, val in enumerate(index):
            
            if i != length:
                diff = index[i + 1] - val 
                
                if diff > result:
                    result = diff


        return result


