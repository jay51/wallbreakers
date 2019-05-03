class Solution:
    def titleToNumber(self, s: str) -> int:
        carry = 26
        sumup = 0
        for i in s:
            sumup = carry * sumup + (ord(i) - ord("A") + 1)

        return sumup

