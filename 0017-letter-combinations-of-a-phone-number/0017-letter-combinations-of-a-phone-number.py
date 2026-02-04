class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """

        _ _ _ _
        ^ ^
        | |
        3 3
        """

        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, currComb, comb):
            if len(digits) == len(currComb):
                comb.append("".join(currComb))
                return
            if i >= len(digits):
                return

            for c in digitsToChar[digits[i]]:
                #include i
                currComb.append(c)
                dfs(i + 1, currComb, comb)
                currComb.pop()

                # #don't include i
                dfs(i + 1, currComb, comb)

        res = []
        dfs(0, [], res)
        return res