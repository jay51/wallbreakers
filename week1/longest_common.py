
def fn(strs):

    if not strs: return ''
   # s1 = min(strs, key=len)
   # s2 = max(strs, key=len)
    s1 = min(strs)
    s2 = max(strs)

    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1



something = ["flower","flow","flight"]
something1 = ["rog","racecar","caar"]
something2 = ["bbc","cc","ba"]
print(fn(something2))
