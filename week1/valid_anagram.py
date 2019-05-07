
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        chars1 = {}
        chars2 = {}

        for char1, char2 in zip(s, t):
            if char1 not in chars1:
                chars1[char1] = 1
            else:
                chars1[char1] += 1

            if char2 not in chars2:
                chars2[char2] = 1
            else:
                chars2[char2] += 1

        for i in chars1:
            if chars1.get(i) != chars2.get(i):
                return False

        return True

