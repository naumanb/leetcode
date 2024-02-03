class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        result = []

        def backtrack(combination,nextDigits):
            if len(nextDigits) == 0:
                result.append(combination)
            else:
                for letter in keyboard[nextDigits[0]]:
                    backtrack(combination+letter, nextDigits[1:])

        backtrack("",digits)
        return result


        