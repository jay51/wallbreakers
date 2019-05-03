# not solved, information is not cleaer
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = str(digits[-1] + 1)
        if "0" not in value:
            digits[-1] = int(value)
        else:
            digits.pop()
            digits += [int(i) for i in list(value)]
        return digits
        
        
