
def fn(s):
    words = []
    for char in s:
        if char.isalpha() or char.isdigit():
            words.append(char.lower())

    reverse = words.copy()
    reverse.reverse()

    print(reverse)
    print(words)
    return words == reverse

something = "A man, a plan, a canal: Panama"
something1 = "race a car"
print(fn(something1))
