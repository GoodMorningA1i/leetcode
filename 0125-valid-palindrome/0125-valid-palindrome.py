class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower()
        newSArr = []
        for c in lowerS:
            if c.isalnum():
                newSArr.append(c)
        convertedS = "".join(newSArr)

        l = 0
        r = len(convertedS) - 1
        while l < r:
            if convertedS[l] != convertedS[r]:
                return False
            l += 1
            r -= 1
        
        return True
