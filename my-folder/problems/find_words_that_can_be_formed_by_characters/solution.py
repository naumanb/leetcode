class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total = 0
        charMap = {}

        for c in chars:
            charMap[c] = chars.count(c)
        
        for word in words:
            match = True
            for c in word:
                if c not in charMap or word.count(c) > charMap[c]:
                    match = False
                    break
            if match:
                total += len(word)
        return total
