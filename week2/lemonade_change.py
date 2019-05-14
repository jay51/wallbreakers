class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                five -= 1
                ten += 1

            if bill == 20:
                five -= 1
                if not ten:
                    five -= 2
                else:
                    ten -= 1
            if five < 0:
                return False

        return True

