
class Solution(object):
    def numJewelsInStones(self, J, S):
      count = 0
      for char in S:
        if char in J:
          count += 1

      return count



J1 = "aA" 
S2 = "aAAbbbb"
J = "z"
S = "ZZ"
print(fn(J, S))
