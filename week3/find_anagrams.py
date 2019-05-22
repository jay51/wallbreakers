
"""
Time : O(n)
Space: O(1)
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = len(p)
        if len(s) < L:
            return []

        want = collections.defaultdict(int)
        have = collections.defaultdict(int)

        for ndx in range(L):
            char_at_p = p[ndx]
            char_at_s = s[ndx]

            want[char_at_p] += 1
            have[char_at_s] += 1

        found = []
        if have == want:found.append(0)

        for i in range(1, len(s)-L+1):
            first_el_in_window = s[i-1]
            last_el_in_window = s[i+L-1]

            have[first_el_in_window] -= 1
            have[last_el_in_window] += 1
            if have[first_el_in_window] == 0:
                del have[first_el_in_window]
            if have == want:
                found.append(i)

        return found

