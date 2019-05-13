# using ascii math
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        asc = 0
        for char in t:
            asc += ord(char) 
        
        for char in s:
            asc -= ord(char) 
            
        return chr(asc)


# using xor math
def findTheDifference(s, t):
    xor = ord(t[0])
    for char in t:
        asc = ord(char) ^ xor
    
    for char in s:
        xor = ord(char) ^ xor 
        
    return chr(xor)

s = "abcd"
t = "abcde"
print(findTheDifference(s, t))


