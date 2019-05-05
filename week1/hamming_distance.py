
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        val = x ^ y

        while val > 0:
            if val & 1:
                dist += 1

            val //=2

        return dist
