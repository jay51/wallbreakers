
class Solution(object):
    def uniqueMorseRepresentations(self, words):
      morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
          "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."]

      offsit = 97
      morse_words = []
      count = []

      for word in words:
        letter = ""
        for char in word:
          letter += morse[ ord(char) - offsit ]

        morse_words.append(letter)

        if letter not in count:
          count.append(letter)

      return len(count)

