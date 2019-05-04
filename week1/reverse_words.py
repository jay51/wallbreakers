class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")
        for ndx, word in enumerate(words):
            words[ndx] = word[::-1]

        return " ".join(words)


