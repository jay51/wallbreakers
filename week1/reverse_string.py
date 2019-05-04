class Solution:
    def reverseString(self, s: List[str]) -> None:

        # s.reverse()
        b = 0
        e = len(s)-1
        while b < e:
            tmp = s[b]
            s[b] = s[e]
            s[e] = tmp
            b += 1
            e -= 1
