# 97 ms runtime beats 85.38% of users with Python3
#
# 16.88 mb beats 50.5% of users with Python3
#

from typing import List, Dict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        goodLetters = {}

        for letter in chars:
            i = 1
            if goodLetters.get(letter):
                i = goodLetters.get(letter) + 1
            goodLetters[letter]=i

        total = 0

        for word in words:
            
            goodLettersCopy = goodLetters.copy()
            goodWord = True

            for letter in word:
                val = goodLettersCopy.get(letter, -1)
                if val > 0:
                    val -= 1
                else:
                    goodWord = False

                    break
                goodLettersCopy[letter] = val
            
            if goodWord:
                total += len(word)

        return total
