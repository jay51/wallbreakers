
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False

        chars1 = defaultdict(int)
        chars2 = defaultdict(int)
        for char1, char2 in zip(s, t):
            chars1[char1] += 1
            chars2[char2] += 1

        for i in chars1:
            if chars1.get(i) != chars2.get(i):
                return False

        return True

       """
       ANOTHER SOLUTION
        if len(t) != len(s): return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
       """

