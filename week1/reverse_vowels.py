class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        found_vowels = [i for i in s if i in vowels]
        s = list(s)
        
        for ndx, val in enumerate(s):
            if val in vowels:
                s[ndx] = found_vowels.pop()
                
        
        return ''.join(s)
