from itertools import permutations

def permute_helper(p, choosen, permute_words):
    print("permute_helper(" + p + ", " + choosen + ",  permute_words  )")

    # if last char in p then choosen is a new string
    if len(p) == 0:
        permute_words.add(choosen)
        print("backTracking")
        return 

    # chosose/explore/unchoose
    for idx, char in enumerate(p):
        # choose
        choosen += char
        rest = p[:idx] + p[idx +1:]
        print("p:", p)
        print("rest:", rest)

        # explore
        permute_helper(rest, choosen, permute_words)
        # unchoose
        choosen = choosen[:-1]


def permute(p):
    words = set()
    permute_helper(p, "", words)
    return words
    
"""
def permute(p):
    if len(p) == 1:
        return p

    result = []
    for idx, char in enumerate(p):
    
    return result
"""

p = "abc"
p = "goo"
print(sorted(permute(p)))

r = ("".join(p) for p in permutations(p))
print(list(r))

