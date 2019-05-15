class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        while g and s:
            print(g)
            print(s)
            if g[-1] <= s[-1]:
                count += 1
                s.pop()
            g.pop()
        return count
