
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = len(p)
        if L < len(p):
            return []
        
        want = collections.defaultdict(int)
        for c in p:
            want[c] += 1
            
        have = collections.defaultdict(int)
        for c in s[:L]:
            have[c] += 1
            
        found = []
        if have == want:
            found.append(0)
        for i in range(1, len(s)-L+1):
            print(i)
            have[s[i-1]] -= 1
            have[s[i+L-1]] += 1
            if have[s[i-1]] == 0:
                del have[s[i-1]]
            if have == want:
                found.append(i)
                
        return found

""" This works but not fast enough"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        phash = {}
        for char in p:
            if char in phash:
                phash[char] += 1
            else: 
                phash[char] = 1

        result = []
        #for idx, char in enumerate(s):
        for idx in range(0, len(s) - (len(p) - 1)):
            string = s[idx: idx + len(p)]
            print(idx)
            if s[idx] not in p:
                continue
                
            if len(string) == len(p):
                shash = {}
                for char in string:
                    if char in shash:
                        shash[char] += 1
                    else:
                        shash[char] = 1
                if shash == phash:
                    result.append(idx)
        return result
                    
s = "cbaebabacd"
p = "abc"

