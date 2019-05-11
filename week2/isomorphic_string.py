
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    # s -> t
    map_s = {}
    # t -> s
    map_t = {}
    
    for i, char_s in enumerate(s):
        char_t = t[i]
        # if no maping found for the current char then add it to map_s
        if char_s not in map_s:
            map_s[char_s] = char_t

        # if no maping found for the current char then add it to map_t
        if char_t not in map_t:
            map_t[char_t] = char_s

        # if both chars map back to each other than continue else return False
        if map_s[char_s] != char_t or map_t[char_t] != char_s:
            return False
    return True

s ="ab"
t = "aa"
print(fn(s, t))
        
