class Solution:
    def findComplement(self, num: int) -> int:
        output = ""
        num = bin(num)[2:]
        for i in num:
            output += "0" if i == "1" else "1"
        
        return int(output, 2) 
